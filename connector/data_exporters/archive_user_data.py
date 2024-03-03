import os
from datetime import datetime

from mage_ai.io.file import FileIO
from mage_ai.settings.repo import get_repo_path
from pandas import DataFrame

if "data_exporter" not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_file(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to filesystem.

    Docs: https://docs.mage.ai/design/data-loading#fileio
    """
    current_datetime = datetime.now()
    current_datetime_str = current_datetime.strftime("%Y-%m-%d-%H")
    filepath = os.path.join(get_repo_path(), "archive", "users", f"{current_datetime_str}.csv")
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    FileIO().export(df, filepath)
    print("User Data Saved Successfully!")
