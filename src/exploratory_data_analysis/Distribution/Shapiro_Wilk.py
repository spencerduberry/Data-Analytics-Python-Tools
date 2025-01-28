#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/spencerduberry/Python_csv/blob/main/Normal_distribution_Shapiro_Wilk.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# In[ ]:


from scipy import stats
import pandas as pd

df = pd.read_csv(
    r"C:\Users\spenc\github\Data_Analytics_Tools_Python\Summative Data.csv"
)


def shapiro_wilk(df: pd.DataFrame, col: str):
    """Performs Shapiro-Wilk test based on dolumn data from a DataFrame

    Args:
    df (pd.DataFrame): The input DataFrame containing the column for the Shapiro-Wilk test
    col (str): The name of the column containing the data to be tested

    Returns
    """
    statistic, p_value = stats.shapiro(df[col])
    return statistic, p_value


def main():
    shapiro_wilk(df, "cr_score")


if __name__ == "__main__":
    main()

# %%
