import vizro.models as vm
import vizro.plotly.express as px
from vizro import Vizro
from vizro.figures import kpi_card, kpi_card_reference
import pandas as pd

# Create a DataFrame for KPI data
df_KPI = pd.DataFrame(
    {
        "WUR KPI": [1.50],
        "WUR target": [1.49],  
        "EUR KPI": [0.29],
        "EUR target": [0.34], 
    }
)


page = vm.Page(
    title="Water & ENERGY USE & Co2 Yeild KPIs",
    components=[
 
        ################################################################
        # WUR
        ##################################################################
        vm.Figure(
            figure=kpi_card(
                data_frame=df_KPI,
                value_column='WUR KPI',
                value_format="{value:.2f}",
                icon="Water",
                title="Water Use Ratio",
            )
        ),
        vm.Figure(
            figure=kpi_card_reference(
                data_frame=df_KPI,
                value_column='WUR KPI',
                reference_column="WUR target",
                value_format="{value:.2f}",  # Added a comma here
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
                value_format="{value:.2f}",
                icon="Energy",
                title="Energy Use Ratio",
            )
        ),
        vm.Figure(
            figure= kpi_card_reference(
                data_frame=df_KPI,
                value_column="EUR KPI",
                reference_column="EUR target",
                value_format="{value:.2f}",
                icon="target",
                title="Energy Use Ratio target",
                
                
            )
        )
    ]
)

# Create and run the dashboard
dashboard = vm.Dashboard(pages=[page])
Vizro().build(dashboard).run()
