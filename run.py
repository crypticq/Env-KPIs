from typing import Union
import pandas as pd
import plotly.graph_objects as go
import vizro.models as vm
import vizro.plotly.express as px
from plotly.subplots import make_subplots
from vizro import Vizro
import vizro.models as vm
from vizro.models.types import capture
from GHG import get_ghg
from waste import get_waste_data
from energy_usage import get_energy_data
from column import column_and_line
import pandas as pd
from water import get_water_data
from vizro.figures import kpi_card, kpi_card_reference


fig_waste = column_and_line(
    data_frame=get_waste_data(),
    x="Year",
    y_column=['total Recycled', 'landfill waste'],  # Columns for bar chart
    y_line='Total Waste Generated')


energy_fig = px.bar(
    get_energy_data(),
    x="Year",
    y='Energy Use',
    title="Total Energy Use (megajoules) (in millions)",
    text_auto=True
)

water_fig = px.bar(
    get_water_data(),
    x="Year",
    y='Total Water Withdrawn (megaliters)',
    title="Water Withdrown",
    text_auto=True
)

fig_ghg = column_and_line(
    data_frame=get_ghg(),
    x="Year",
    y_column=["Scope 1", "Scope 2", "Scope 3"],
    y_line='Total GHG Manufacturing (Scopes 1, 2 and 3)')


page = vm.Page(
    title="GHG",
    layout=vm.Layout(grid=[[0,0,1]]),
    components=[
        vm.Graph(figure=fig_ghg),
        vm.Graph(figure=px.funnel_area(get_ghg(), names="Year", values="Total GHG Manufacturing (Scopes 1, 2 and 3)")
)


    ]
)

page_two=vm.Page(
    title="Waste data (Data Taken from SEC)",
    components=[
        vm.Graph(figure=fig_waste),
    ]
)

page_three=vm.Page(
    title="Energy Useage",
    components=[
       vm.Graph(figure=energy_fig)
    ]
)

page_four=vm.Page(
    title="Water",
    components=[
       vm.Graph(figure=water_fig)
    ]
)



df_KPI=pd.DataFrame(
    {
        "CO2 Yield KPI": [60],
        "Co2 Target": [60],
        "WUR KPI": [1.50],
        "WUR target": [1.49],
        "EUR KPI": [0.29],
        "EUR target": [0.34],
    }
)


KPI_summary=vm.Page(
    title="Water & ENERGY USE & Co2 Yeild KPIs",
    components=[
        ################################################################
        # WUR
        ##################################################################
        vm.Figure(
            figure=kpi_card(
                data_frame=df_KPI,
                value_column='WUR KPI',
                icon="Water",
                title="Water Use Ratio",
            )
        ),
        vm.Figure(
            figure=kpi_card_reference(
                data_frame=df_KPI,
                value_column='WUR KPI',
                reference_column="WUR target",
                icon="target",
                title="Water Use Ratio Target",
            )
        ),
        ##################################################################
        # EUR
        ##################################################################
        vm.Figure(
            figure=kpi_card(
                data_frame=df_KPI,
                value_column="EUR KPI",
                icon="Energy",
                title="Energy Use Ratio",
            )
        ),
        vm.Figure(
            figure=kpi_card_reference(
                data_frame=df_KPI,
                value_column="EUR KPI",
                reference_column="EUR target",
                icon="target",
                title="Energy Use Ratio target",
                reverse_color=True


            )
        )
    ]
)

dashboard=vm.Dashboard(
    pages=[KPI_summary, page, page_two, page_three, page_four])
Vizro().build(dashboard).run()
