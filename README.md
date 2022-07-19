# AI projects using Kedro Workflow
This repository contains all my AI projects using Kedro Workflow. 

## What is Kedro?
[Kedro](https://kedro.org/) is an open-source Python framework for creating reproducible, maintainable, and modular data science code. It borrows concepts from software engineering and applies them to machine-learning code; applied concepts include modularity, separation of concerns and versioning.

For the source code, take a look at the [Kedro repository on Github](https://github.com/kedro-org/kedro)

## Installation Prerequisites
* Kedro supports macOS, Linux and Windows (7 / 8 / 10 and Windows Server 2016+). If you encounter any problems on these platforms, please check the frequently asked questions, GitHub Discussions or the Discord Server.
* To work with Kedro, we highly recommend that you download and install Anaconda (Python 3.x version).
* If you are using PySpark, you will also need to install Java. If you are a Windows user, you will need admin rights to complete the installation.

## Virtual Environments
```shell
conda create --name kedro-env python=3.8
conda activate kedro-env
```
## Installing & Initializing Kedro Project
Installing Kedro from the Python Package Index (PyPI)

```shell
pip install kedro
```

Installing Kedro with Conda

```shell
conda install -c conda-forge kedro
```

Verify a successful installation

```shell
kedro info
```

You should see an ASCII art graphic and the Kedro version number. For example:
<br><br>
<img src='images/kedro_graphic.png' width='30%'>

## Creating a new Project with Kedro

```shell
kedro new
```

## Experiment Tracking usage

To enable [experiment tracking](https://kedro.readthedocs.io/en/stable/08_logging/02_experiment_tracking.html) in Kedro-Viz, you need to add the Kedro-Viz `SQLiteStore` to your Kedro project.

This can be done by adding the below code to `settings.py` in the `src` folder of your Kedro project.

```python
from kedro_viz.integrations.kedro.sqlite_store import SQLiteStore
from pathlib import Path
SESSION_STORE_CLASS = SQLiteStore
SESSION_STORE_ARGS = {"path": str(Path(__file__).parents[2] / "data")}
```