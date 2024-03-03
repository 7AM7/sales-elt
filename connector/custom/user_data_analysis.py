if "custom" not in globals():
    from mage_ai.data_preparation.decorators import custom

import pandas as pd


@custom
def transform_custom(df, *args, **kwargs):
    unique_values_check = df.nunique() == len(df)  # Check for unique values in each column
    duplicated_rows_count = df.duplicated().sum()  # Count duplicated rows
    nans_count = df.isna().sum()  # Count NaNs in each column

    analysis_results = pd.DataFrame(
        {"Column": df.columns, "Unique_Values": unique_values_check, "NaNs_Count": nans_count}
    )

    additional_info = pd.DataFrame(
        {
            "Column": ["Duplicated_Rows"],
            "Unique_Values": [False],
            "NaNs_Count": [duplicated_rows_count],
        }
    )

    analysis_results = pd.concat([analysis_results, additional_info], ignore_index=True)

    return analysis_results
