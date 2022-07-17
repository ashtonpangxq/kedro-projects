"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.2
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from category_encoders import CountEncoder
from typing import List


def _clean(df: pd.DataFrame) -> pd.DataFrame:
    df["Exterior2nd"] = df["Exterior2nd"].replace({"Brk Cmn": "BrkComm"})
    df["GarageYrBlt"] = df["GarageYrBlt"].where(df.GarageYrBlt <= 2010, df.YearBuilt)

    df.rename(
        columns={
            "1stFlrSF": "FirstFlrSF",
            "2ndFlrSF": "SecondFlrSF",
            "3SsnPorch": "Threeseasonporch",
        },
        inplace=True,
    )

    return df


def _filling_missing_values(df: pd.DataFrame) -> pd.DataFrame:

    df["PoolQC"] = df["PoolQC"].fillna("no")
    df["MiscFeature"] = df["MiscFeature"].fillna("no")
    df["Alley"] = df["Alley"].fillna("no")
    df["Fence"] = df["Fence"].fillna("no")
    df["FireplaceQu"] = df["FireplaceQu"].fillna("no")
    df["GarageCond"] = df["GarageCond"].fillna("no")
    df["GarageQual"] = df["GarageQual"].fillna("no")
    df["GarageFinish"] = df["GarageFinish"].fillna("no")
    df["BsmtExposure"] = df["BsmtExposure"].fillna("no")
    df["BsmtCond"] = df["BsmtCond"].fillna("no")
    df["BsmtQual"] = df["BsmtQual"].fillna("no")
    df["BsmtFinType2"] = df["BsmtFinType2"].fillna("no")
    df["BsmtFinType1"] = df["BsmtFinType1"].fillna("no")
    df["Fence"] = df["Fence"].fillna("no")
    df["MasVnrType"] = df["MasVnrType"].fillna("no")
    df["GarageYrBlt"] = df["GarageYrBlt"].fillna(0)
    df["GarageType"] = df["GarageType"].fillna(0)
    df["GarageArea"] = df["GarageArea"].fillna(0)
    df["GarageCars"] = df["GarageCars"].fillna(0)
    df["BsmtFinSF1"] = df["BsmtFinSF1"].fillna(0)
    df["BsmtFinSF2"] = df["BsmtFinSF2"].fillna(0)
    df["MasVnrArea"] = df["MasVnrArea"].fillna(0)
    df["BsmtFullBath"] = df["BsmtFullBath"].fillna(0)
    df["BsmtHalfBath"] = df["BsmtHalfBath"].fillna(0)
    df["BsmtUnfSF"] = df["BsmtUnfSF"].fillna(0)
    df["TotalBsmtSF"] = df["TotalBsmtSF"].fillna(0)

    return df


def _category_encoding(train_df: pd.DataFrame, cat_df: pd.DataFrame) -> pd.DataFrame:
    enc = CountEncoder(normalize=True, cols=cat_df.columns)
    return enc.fit_transform(train_df)


def preprocess_train(df: pd.DataFrame) -> pd.DataFrame:
    df = _clean(df)
    df = _filling_missing_values(df)

    df.drop("LotFrontage", axis=1, inplace=True)
    df.drop("Electrical", axis=1, inplace=True)

    cat_df = df.select_dtypes(include="object")
    df = _category_encoding(df, cat_df)

    df = df.drop(["Id"], axis=1)

    return df


def preprocess_test(df: pd.DataFrame) -> pd.DataFrame:
    df = _clean(df)
    df = _filling_missing_values(df)

    df.drop("LotFrontage", axis=1, inplace=True)
    df.drop("Electrical", axis=1, inplace=True)

    cat_df = df.select_dtypes(include="object")
    df = _category_encoding(df, cat_df)

    df = df.drop(["Id"], axis=1)

    return df
