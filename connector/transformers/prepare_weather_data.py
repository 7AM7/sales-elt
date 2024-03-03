from datetime import datetime
from os import path

import pandas as pd
import requests
from mage_ai.io.config import ConfigFileLoader
from mage_ai.settings.repo import get_repo_path

if "transformer" not in globals():
    from mage_ai.data_preparation.decorators import transformer
if "test" not in globals():
    from mage_ai.data_preparation.decorators import test


def get_weather(row, api_key, base_url):
    params = {
        "lat": row["address.geo.lat"],
        "lon": row["address.geo.lng"],
        "units": "metric",  # Fetch temperature in Celsius (use "imperial" for Fahrenheit)
        "appid": api_key,
    }

    owm_response = requests.get(base_url, params=params, verify=False)
    owm_response_json = owm_response.json()

    return pd.Series(
        {
            "weather_date": pd.to_datetime(datetime.now().strftime("%Y/%m/%d")),
            "weather_lat": row["address.geo.lat"],
            "weather_lng": row["address.geo.lng"],
            "weather_temperature": owm_response_json["main"]["temp"],
            "weather_conditions": owm_response_json["weather"][0]["main"],
        }
    )


@transformer
def load_data_from_api(user_df: pd.DataFrame, *args, **kwargs):
    """
    Template for loading data from API
    """
    config_path = path.join(get_repo_path(), "io_config.yaml")
    config_profile = "default"
    config = ConfigFileLoader(config_path, config_profile)
    api_key = config["WEATHER_API_KEY"]
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    df_weather = user_df.apply(lambda x: get_weather(x, api_key, base_url), axis=1)

    return df_weather


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    expected_cols = [
        "weather_date",
        "weather_lat",
        "weather_lng",
        "weather_temperature",
        "weather_conditions",
    ]

    assert set(expected_cols).issubset(set(output.columns))
