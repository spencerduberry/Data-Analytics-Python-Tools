import pandas as pd

# DataFrame and column name taken as input. Dataframe returned.
def encode_col(df: pd.DataFrame, col:str) -> pd.DataFrame:
    df[f'{col}_encoded'] = df[col].map({k: i for i, k in enumerate(sorted(df["gender"].unique()))})
    return df