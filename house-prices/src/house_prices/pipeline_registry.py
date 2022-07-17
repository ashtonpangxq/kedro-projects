"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline
from house_prices.pipelines import data_processing
from house_prices.pipelines import modelling as mod


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    data_processing_pipeline = data_processing.create_pipeline()
    modelling_pipeline = mod.create_pipeline(
        model_types=["linear_regression", "random_forest"]
    )

    return {
        "__default__": data_processing_pipeline + modelling_pipeline,
        "Data Ingestion": data_processing_pipeline,
        "Modelling Stage": modelling_pipeline,
    }
