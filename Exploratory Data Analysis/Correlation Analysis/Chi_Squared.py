#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from scipy.stats import chi2_contingency


def chi_squared(df: pd.DataFrame, col_1: str, col_2: str):
    """Performs a chi-squared test based on data from two columns in a DataFrame

    Args:
        df (pd.DataFrame): The input DataFrame containing teh columsn for the chi-squared test
        col_1 (str): The name of the volumn containing the dependent variable
        col_1 (str): The name of the volumn containing the independent variable

    Returns:
        chi2 (float): The chi-squared result of comparing the two columns
        p (float): the probability of observing a
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

    print("Chi-Squared Statistic:", chi2)
    print("p-value:", p)
    print("Degrees of Freedom:", dof)
    print("Expected Frequencies:\n", expected)

    alpha = 0.05
    if p < alpha:
        print(
            "Reject the null hypothesis: There is a significant association between the variables."
        )
    else:
        print(
            "Fail to reject the null hypothesis: There is no significant association between the variables."
        )
