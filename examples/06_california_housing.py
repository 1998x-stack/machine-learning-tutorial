#!/usr/bin/env python3
"""Geographically held-out California Housing regression exercise.

Requires internet access for the first fetch. This historical block-group
dataset is not contemporary individual-home market pricing.
"""
from pathlib import Path
import joblib
import numpy as np
from sklearn.base import clone
from sklearn.datasets import fetch_california_housing
from sklearn.dummy import DummyRegressor
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import GroupShuffleSplit
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

def main():
    housing = fetch_california_housing(as_frame=True)
    X, y = housing.data, housing.target
    assert {"Latitude", "Longitude"}.issubset(X.columns)
    # A coarse grid is a teaching proxy for geographic independence,
    # not proof that test groups represent deployment regions.
    groups = (np.floor(X["Latitude"] * 2).astype(int).astype(str) + "_" +
              np.floor(X["Longitude"] * 2).astype(int).astype(str))
    outer = GroupShuffleSplit(n_splits=1, test_size=0.20, random_state=42)
    dev_ids, test_ids = next(outer.split(X, y, groups))
    Xdev, Xtest = X.iloc[dev_ids], X.iloc[test_ids]
    ydev, ytest = y.iloc[dev_ids], y.iloc[test_ids]
    gdev, gtest = groups.iloc[dev_ids], groups.iloc[test_ids]
    inner = GroupShuffleSplit(n_splits=1, test_size=0.25, random_state=42)
    train_loc, val_loc = next(inner.split(Xdev, ydev, gdev))
    Xtrain, Xval = Xdev.iloc[train_loc], Xdev.iloc[val_loc]
    ytrain, yval = ydev.iloc[train_loc], ydev.iloc[val_loc]
    gtrain, gval = gdev.iloc[train_loc], gdev.iloc[val_loc]
    assert set(gtrain).isdisjoint(set(gval))
    assert set(gdev).isdisjoint(set(gtest))
    models = {
        "constant": DummyRegressor(strategy="mean"),
        "ridge": make_pipeline(SimpleImputer(strategy="median"),
                               StandardScaler(), Ridge(alpha=30.0)),
        "boosted_trees": HistGradientBoostingRegressor(
            max_iter=100, max_leaf_nodes=15, learning_rate=0.06,
            random_state=42),
    }
    val_rmse = {}
    for name, model in models.items():
        candidate = clone(model).fit(Xtrain, ytrain)
        val_rmse[name] = float(np.sqrt(
            mean_squared_error(yval, candidate.predict(Xval))))
    selected_name = min(val_rmse, key=val_rmse.get)
    final = clone(models[selected_name]).fit(Xdev, ydev)
    test_pred = final.predict(Xtest)
    print("historical dataset n:", len(y))
    print("geographic groups train/val/test:",
          len(set(gtrain)), len(set(gval)), len(set(gtest)))
    print("validation RMSE by candidate (100k USD units):", val_rmse)
    print("selected model:", selected_name)
    print("held-out test MAE:", mean_absolute_error(ytest, test_pred))
    print("held-out test RMSE:", np.sqrt(mean_squared_error(ytest, test_pred)))
    out = Path("models") / "california_housing.joblib"
    out.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump({"model": final, "feature_order": X.columns.tolist(),
                 "source": "scikit-learn fetch_california_housing",
                 "units": "historical median house value, 100k USD"}, out)
    print("model saved:", out, "(only load trusted model files)")

if __name__ == "__main__":
    main()
