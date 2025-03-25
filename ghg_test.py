from typing import Union
import pandas as pd
import plotly.graph_objects as go
import vizro.models as vm
import vizro.plotly.express as px
from plotly.subplots import make_subplots
from vizro import Vizro
from vizro.models.types import capture
from column import column_and_line



data_ghg = pd.DataFrame(
    {
        "Year": [2021, 2022, 2023],
        "Scope 1": [325833, 304144, 292106],
        "Scope 2": [869832, 890400, 844848],
        "Scope 3": [4299247, 4363071, 4484403],
        'Total GHG Manufacturing (Scopes 1, 2 and 3)':[325833+869832+4299247, 304144+890400+4363071,292106+844848+4484403]
    }
)






# Create the figure
fig = column_and_line(
    data_frame=data_ghg,
    x="Year",
    y_column=["Scope 1", "Scope 2", "Scope 3"],  # Columns for bar chart
    y_line= 'Total GHG Manufacturing (Scopes 1, 2 and 3)')

# Create the Vizro page
page = vm.Page(
    title="GHG Emissions",
    components=[
        vm.Tabs(
            tabs=[
                vm.Container(
                    title="Scope 1 Emissions (Metric Tons CO2 Eq)",
                    components=[
                        vm.Graph(
                            figure=fig,  # Use the figure directly
                        ),
                    ],
                ),
            ],
        ),
    ],
)

# Create the dashboard
dashboard = vm.Dashboard(pages=[page])

# Build and run the dashboard
Vizro().build(dashboard).run()
