# Predicting House Prices

## Overview
Predicting House Prices with [Kaggle Dataset](https://www.kaggle.com/c/house-prices-advanced-regression-techniques) using Machine Learning Models. 

Current Models used:
* Linear Regression
* Random Forest
* Ridge Regression
* Lasso Regression

## How to install dependencies

Declare any dependencies in `src/requirements.txt` for `pip` installation and `src/environment.yml` for `conda` installation.

To install them, run:

```
pip install -r src/requirements.txt
```

## How to run your Kedro pipeline

You can run your Kedro project with:

```
kedro run
```

## How to test your Kedro project

To be added.

Have a look at the file `src/tests/test_run.py` for instructions on how to write your tests. You can run your tests as follows:

```
kedro test
```

To configure the coverage threshold, go to the `.coveragerc` file.

### Jupyter
To use Jupyter notebooks in your Kedro project, you need to install Jupyter:

```
pip install jupyter
```

After installing Jupyter, you can start a local notebook server:

```
kedro jupyter notebook
```

### IPython
And if you want to run an IPython session:

```
kedro ipython
```

### Creating Documentation with Kedro

```shell
kedro build-docs
```

Documentation is located under docs/build/html

### Experimental Tracking

Kedro have an inbuilt experimental tracking system that is viewable under Kedro Viz.

An alternative is MLFlow Tracking System which uses kedro-mlflow module.

### MLFlow Tracking

After you have run several experiments, you can access MLFlow experimental tracking features under:

```shell
kedro mlflow ui
```