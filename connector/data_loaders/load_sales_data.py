import os

from mage_ai.settings.repo import get_repo_path

if "data_loader" not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if "test" not in globals():
    from mage_ai.data_preparation.decorators import test

import pandas as pd


@data_loader
def load_data_from_file(*args, **kwargs):
    """
    Template for loading data from filesystem.
    Load data from csv file.

    """

    filepath = os.path.join(get_repo_path(), "data/sales_data.csv")
    sales_df = pd.read_csv(filepath)

    return sales_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    expected_cols = ["order_id", "customer_id", "quantity", "product_id", "price", "order_date"]

    assert set(expected_cols).issubset(set(output.columns))
