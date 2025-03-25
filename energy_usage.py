import pandas as pd


def get_energy_data():
    df = pd.DataFrame(
        {
            "Year":[2021,2022,2023],
            "Energy Use": [63735.8, 65389, 66803]
        }
    )
    return df