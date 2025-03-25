from typing import Union

import pandas as pd
import plotly.graph_objects as go
import vizro.models as vm
import vizro.plotly.express as px
from plotly.subplots import make_subplots
from vizro import Vizro
from vizro.models.types import capture



# total metric tons of CO2-equivalent
def get_ghg():
    data_ghg = {
        "Year": [2021, 2022, 2023],
        "Scope 1": [325833, 304144, 292106],
        "Scope 2": [869832, 890400, 844848],
        "Scope 3": [4299247, 4363071, 4484403],
        'Total GHG Manufacturing (Scopes 1, 2 and 3)':[325833+869832+4299247, 304144+890400+4363071,292106+844848+4484403]
    }

    return pd.DataFrame(data_ghg)


