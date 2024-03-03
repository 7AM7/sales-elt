import pandas as pd


def transform_custom(df):
    unique_values_check = df.nunique() == len(df)
    duplicated_rows_count = df.duplicated().sum()
    nans_count = df.isna().sum()

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
