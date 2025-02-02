import pandas as pd


def aggregate(df: pd.DataFrame, col_1: str, col_2: str, agg_func):
    """
    Args:
        df (pd.DataFrame): a DataFrame containing two columns to be aggregated
        col_1 (str): a column to be used as input in an aggreagation function
        col_2 (str): a column to be used as input in an aggreagation function
        agg_func (_type_): an aggregation function

    Returns:
        transformed (aggregated) data
    """
    df["new_data"] = agg_func(df[col_1], df[col_2])
    return df["new_data"]


def binarise(df: pd.DataFrame, col_1: str, col_val: str):
    """_summary_

    Args:
        df (pd.DataFrame): a DataFrame containing a column to be converted to binary
        col_1 (str): a column to be converted to binary
        col_val (str): a value within a column to be converted to binary

    Returns:
        modifed DataFrame with a column converted to binary
    """
    df["binary_data"] = df[col_1].apply(lambda x: 1 if x == col_val else 0)
    return df


def encode_col(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """Encodes a column of a Dataframe by mapping unique values to integers

    Args:
        df (pd.DataFrame): The input DataFrame containing the column to be encoded
        col (str): The name of the column to be encoded

    Returns:
        pd.DataFrame: A DataFrame containing the encoded column in addition to the original data
    """
    df[f"{col}_encoded"] = df[col].map(
        {k: i for i, k in enumerate(sorted(df[col].unique()))}
    )
    return df
