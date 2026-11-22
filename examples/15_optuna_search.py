#!/usr/bin/env python3
"""Optional Optuna trial search for a small RBF SVC on Iris.

Requires: Python 3.10+, scikit-learn, numpy, optuna.
This runs actual CV trials, refits on development data and evaluates one
held-out test set only after the search has finished.
"""
import numpy as np
import optuna
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import balanced_accuracy_score

X, y = load_iris(return_X_y=True)
Xdev, Xtest, ydev, ytest = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=15)
cv = StratifiedKFold(n_splits=3, shuffle=True, random_state=15)

def objective(trial: optuna.trial.Trial) -> float:
    c = trial.suggest_float("C", 0.01, 100.0, log=True)
    gamma = trial.suggest_float("gamma", 0.001, 10.0, log=True)
    pipeline = make_pipeline(
        StandardScaler(), SVC(kernel="rbf", C=c, gamma=gamma))
    scores = cross_val_score(
        pipeline, Xdev, ydev, cv=cv,
        scoring="balanced_accuracy", n_jobs=1)
    return float(scores.mean())

study = optuna.create_study(
    direction="maximize",
    sampler=optuna.samplers.TPESampler(seed=15))
study.optimize(objective, n_trials=12, show_progress_bar=False)
print("completed trials:", len(study.trials))
print("best development CV:", study.best_value)
print("best parameters:", study.best_params)

final = make_pipeline(
    StandardScaler(), SVC(kernel="rbf", **study.best_params))
final.fit(Xdev, ydev)
pred = final.predict(Xtest)
print("held-out balanced accuracy:",
      balanced_accuracy_score(ytest, pred))
assert pred.shape == ytest.shape
assert np.all(np.isfinite(pred))
