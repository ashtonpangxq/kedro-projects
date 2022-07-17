"""
This is a boilerplate pipeline 'modelling'
generated using Kedro 0.18.2
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import evaluate_model, split_data, train_model

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([])
