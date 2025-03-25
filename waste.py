import pandas as pd


def get_waste_data():
    data = {
        "Year": [2020, 2021, 2022, 2023],
        "Total Waste Generated": [185654+43587, 155822+55971, 147371+116570, 141703+30000],
        "landfill waste": [185654, 155822, 147371, 141703],
        "total Recycled": [43587, 55971, 116570, 30000],  # Adjusted for 2023
        
    }

    return pd.DataFrame(data)