import pandas as pd
import requests

if "data_loader" not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if "test" not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to fetch data: {response.status_code}")
        return

    # Convert the JSON response to a pandas DataFrame
    user_df = pd.json_normalize(response.json())
    return user_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    expected_cols = ["id", "name", "email", "address.geo.lat", "address.geo.lng"]

    assert set(expected_cols).issubset(set(output.columns))
