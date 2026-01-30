"""Ancilliary scripts to help with Exploratory Data Analysis"""
from typing import Tuple
from pandas import DataFrame

def detect_outliers(dataframe: DataFrame,
                    column_name: str,
                    mild: bool = True)  -> Tuple[DataFrame, DataFrame]:
    """
    Use IQR to find the lower & higher outliers in a dataframe's column.

    Args:
        dataframe (DataFrame): The relevant DataFrame
        column_name (str): Column name as string
        mild (bool): Whether to detect mild (True) or extreme (false) outliers

    Returns:
        Tuple[DataFrame, DataFrame]: Lower outliers, higher outliers
    """
    multiplier: float = 1.0
    if mild:
        multiplier *= 1.5
    else:
        multiplier *= 3.0
    first_quartile: float = dataframe[column_name].quantile(0.25)
    third_quartile: float = dataframe[column_name].quantile(0.75)
    inter_quartile_range: float = third_quartile - first_quartile
    lower_bound: float = first_quartile - multiplier * inter_quartile_range
    upper_bound: float = third_quartile + multiplier * inter_quartile_range
    lower_outliers: DataFrame = dataframe[(dataframe[column_name] < lower_bound)]
    higher_outliers: DataFrame = dataframe[(upper_bound < dataframe[column_name])]
    return lower_outliers, higher_outliers

def print_outlier_count_and_percentage_report(count_lower_outliers: int,
                         count_higher_outliers: int,
                         dataframe_name: str,
                         dataframe_row_count: int,
                         column_name: str,
                         mild: bool = True) -> None:
    """Print an outlier report.

    Args:
        lower_outliers (int): The number of lower outliers
        higher_outliers (int): The number higher outliers
        dataframe_name (str): Original dataframe name
        dataframe_row_count (int): The number of rows in the original dataframe
        column_name (str): Original data column name
        mild (bool): Whether to report mild (True) or extreme (false) outliers
    """
    # all outliers
    count_all_outliers = count_lower_outliers + count_higher_outliers
    percent_all_outliers = round(count_all_outliers/dataframe_row_count*100, 2)
    # lower outliers
    percent_lower_outliers = round(count_lower_outliers/dataframe_row_count*100, 2)
    # higher outliers
    percent_higher_outliers = round(count_higher_outliers/dataframe_row_count*100, 2)
    preamble = None
    if mild:
        preamble = 'Mild'
    else:
        preamble = 'EXTREME'
    # print report
    print(f'=== {preamble} Outlier Report: {dataframe_name}.{column_name} ===')
    print(f'All: {count_all_outliers} ({percent_all_outliers}%)')
    print(f'Lower: {count_lower_outliers} ({percent_lower_outliers}%)')
    print(f'Higher: {count_higher_outliers} ({percent_higher_outliers}%)')

def quick_outlier_report(dataframe: DataFrame,
                         dataframe_name: str,
                         column_name: str,
                         mild: bool = True) -> None:
    """Quickly generate an outlier report.

    Args:
        dataframe (DataFrame): The data
        dataframe_name (str): The name of the dataframe
        column_name (str): Name of the column to examine
        mild (bool): Whether to report mild (True) or extreme (false) outliers
    """
    lower, higher = detect_outliers(dataframe, column_name, mild)
    print_outlier_count_and_percentage_report(lower.shape[0],
                                              higher.shape[0],
                                              dataframe_name,
                                              dataframe.shape[0],
                                              column_name,
                                              mild)
    