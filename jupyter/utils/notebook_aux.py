"""Ancilliary scripts to help with Exploratory Data Analysis"""
from typing import Tuple
from pandas import DataFrame

def detect_outliers(dataframe: DataFrame,
                    column_name: str)  -> Tuple[DataFrame, DataFrame]:
    """
    Use IQR to find the lower & higher outliers in a dataframe's column.

    Args:
        dataframe (DataFrame): The relevant DataFrame
        column_name (str): Column name as string

    Returns:
        Tuple[DataFrame, DataFrame]: Lower outliers, higher outliers
    """
    first_quartile = dataframe[column_name].quantile(0.25)
    third_quartile = dataframe[column_name].quantile(0.75)
    inter_quartile_range = third_quartile - first_quartile
    lower_bound = first_quartile - 1.5 * inter_quartile_range
    upper_bound = third_quartile + 1.5 * inter_quartile_range
    lower_outliers = dataframe[(dataframe[column_name] < lower_bound)]
    higher_outliers = dataframe[(upper_bound < dataframe[column_name])]
    return lower_outliers, higher_outliers

def print_outlier_count_and_percentage_report(count_lower_outliers: int,
                         count_higher_outliers: int,
                         dataframe_name: str,
                         dataframe_row_count: int,
                         column_name: str) -> None:
    """Print an outlier report.

    Args:
        lower_outliers (int): The number of lower outliers
        higher_outliers (int): The number higher outliers
        dataframe_name (str): Original dataframe name
        dataframe_row_count (int): The number of rows in the original dataframe
        column_name (str): Original data column name
    """
    # all outliers
    count_all_outliers = count_lower_outliers + count_higher_outliers
    percent_all_outliers = round(count_all_outliers/dataframe_row_count*100, 2)
    # lower outliers
    percent_lower_outliers = round(count_lower_outliers/dataframe_row_count*100, 2)
    # higher outliers
    percent_higher_outliers = round(count_higher_outliers/dataframe_row_count*100, 2)
    # print report
    print(f'=== Outlier Report:{dataframe_name}.{column_name} ===')
    print(f'All: {count_all_outliers} ({percent_all_outliers}%)')
    print(f'Lower: {count_lower_outliers} ({percent_lower_outliers}%)')
    print(f'Higher: {count_higher_outliers} ({percent_higher_outliers}%)')
