"""Offers functions to manage data resources"""
import pandas as pd


def load_enriched_data_into_main(table_name: str) -> pd.DataFrame:
    """Build a dataframe using enriched data.

    Args:
        table_name (str): Name of the table as string

    Returns:
        pd.DataFrame: _description_
    """
    result = pd.read_csv(f'./data/enriched/{table_name}_enr.csv', index_col=0)
    # set the created_at timestamp to datetime type
    result['created_at'] = pd.to_datetime(
        result['created_at'],
        format='%Y-%m-%d %H:%M:%S')
    return result
