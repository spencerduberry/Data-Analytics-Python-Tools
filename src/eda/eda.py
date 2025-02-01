import pandas as pd
from scipy import stats
from scipy.stats import chi2_contingency
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
import ydata_profiling


# Correlation
def chi_squared(df: pd.DataFrame, col_1: str, col_2: str):
    """Performs a chi-squared test based on data from two columns in a DataFrame

    Args:
        df (pd.DataFrame): The input DataFrame containing the columns for the chi-squared test
        col_1 (str): The name of the column containing the dependent variable
        col_1 (str): The name of the column containing the independent variable

    Returns:
        chi2 (float): The chi-squared result of comparing the two columns
        p (float): The probability of observing a
                   test statistic as extreme or more extreme
                   than the one calculated, assuming the null
                   hypothesis (no association between the variables)
                   is true.
        dof (int): The degrees of freedom of the chi-squared test.
                  Calculated as (number of rows - 1) * (number of columns - 1)
                  in the contingency table.
        expected (numpy.ndarray): The array of expected frequencies for each cell
                  in the contingency table, assuming the null hypothesis is true.
    """

    contingency_table = pd.crosstab(df[col_1], df[col_2])
    chi2, p, dof, expected = chi2_contingency(contingency_table)

    return chi2, p, dof, expected


# Distribution
def shapiro_wilk(df: pd.DataFrame, col: str):
    """Performs Shapiro-Wilk test based on column data from a DataFrame

    Args:
    df (pd.DataFrame): The input DataFrame containing the column for the Shapiro-Wilk test
    col (str): The name of the column containing the data to be tested

    Returns
    """
    statistic, p_value = stats.shapiro(df[col])
    return statistic, p_value


# Proximity
def cos_sim(df: pd.DataFrame, col_1: str):
    """
    Calculates cosine similarity for a given column in a DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.
        col_1 (str): The name of the column to calculate cosine similarity for.

    Returns:git rm data_profile.ipynb
        np.ndarray: A matrix of cosine similarities.
    """
    data = df[[col_1]]
    scaler = StandardScaler()
    balances_scaled = scaler.fit_transform(data)
    cosine_similarities = cosine_similarity(balances_scaled)

    return cosine_similarities


# EDA
def profile_data(df):
    profile = ydata_profiling.ProfileReport(df)
    profile.to_file("profile.html")
