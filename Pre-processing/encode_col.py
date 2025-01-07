import pandas as pd

def encode_col(df: pd.DataFrame, col:str) -> pd.DataFrame:
    """Encodes a column of a Dataframe by mapping unique values to integers

    Args:
        df (pd.DataFrame): The input DataFrame containing the column to be encoded
        col (str): The name of the column to be encoded

    Returns:
        pd.DataFrame: A DataFrame containing the encoded column in addition to the original data
    """
    df[f'{col}_encoded'] = df[col].map({k: i for i, k in enumerate(sorted(df[col].unique()))})
    return df