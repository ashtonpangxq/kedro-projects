"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.2
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import preprocess_train, preprocess_test


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=preprocess_train,
                inputs="train",
                outputs="preprocessed_train",
                name="preprocess_train_node",
            ),
            node(
                func=preprocess_test,
                inputs="test",
                outputs="preprocessed_test",
                name="preprocess_test_node",
            ),
        ],
        namespace="ingestion",
        inputs=["train", "test"],
        outputs=["preprocessed_train", "preprocessed_test"],
    )
