"""
This is a boilerplate pipeline 'modelling'
generated using Kedro 0.18.2
"""
import importlib
from typing import Any, Dict, Tuple
import pandas as pd
import numpy as np

from sklearn.base import BaseEstimator
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error, max_error
from sklearn import metrics

SCALER = StandardScaler()


def split_data(data: pd.DataFrame, split_options: Dict) -> Tuple:
    target_variable = split_options["target"]
    independent_variables = [x for x in data.columns if x != target_variable]
    test_size = split_options["test_size"]
    random_state = split_options["random_state"]

    x = data[independent_variables]
    y = data[target_variable]
    X_train, X_test, y_train, y_test = train_test_split(
        x, y, test_size=test_size, random_state=random_state
    )

    return X_train, X_test, y_train, y_test


def train_model(
    X_train: pd.DataFrame, y_train: pd.Series, model_options: Dict[str, Any]
) -> Tuple[BaseEstimator, Dict[str, Any]]:
    """Trains the linear regression model.
    Args:
        X_train: Training data of independent features.
        y_train: Training data for price.
    Returns:
        Trained model.
    """

    # Parse parameters
    model_module = model_options.get("module")
    model_type = model_options.get("class")
    model_arguments = model_options.get("kwargs")

    # Import and instantiate Sklearn regressor object
    regressor_class = getattr(importlib.import_module(model_module), model_type)
    regressor_instance = regressor_class(**model_arguments)

    # Fit model
    X_train = SCALER.fit_transform(X_train)
    regressor_instance.fit(X_train, y_train)
    flat_model_params = {**{"model_type": model_type}, **model_arguments}
    return regressor_instance, flat_model_params


def evaluate_model(
    regressor: BaseEstimator,
    X_test: pd.DataFrame,
    y_test: pd.Series,
) -> Dict[str, float]:
    """Calculates and logs the coefficient of determination.
    Args:
        regressor: Trained model.
        X_test: Testing data of independent features.
        y_test: Testing data for price.
    """

    # Predictions
    X_test = SCALER.transform(X_test)
    y_pred = regressor.predict(X_test)\
    
    # Model Evaluation
    score = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    me = max_error(y_test, y_pred)

    return {"r2_score": score, "mse": mse, "mae": mae, "max_error": me}
