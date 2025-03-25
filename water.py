import pandas as pd


def get_water_data():
    df = pd.DataFrame(
        {
            "Year":[2021,2022,2023],
            "Total Water Withdrawn (megaliters)": [298235, 308736, 311998]
        }
    )
    return df