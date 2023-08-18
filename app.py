import dash_bootstrap_components as dbc
import pandas as pd
from dash import *
from dash import html
import plotly.express as px

# Initializes app variable for project

app = dash.Dash(external_stylesheets=[dbc.themes.PULSE])
server = app.server

# Import csv data for current US Covid-tracking data
df = pd.read_csv("./data/national-history.csv")


def graph_generator(value):
    """
    This function returns the Y value for the covid_graph
    :param value:
    :return:
    """
    figure = px.bar(df, x='date', y=value)
    return figure


app.layout = html.Div(
    children=[
        html.H1('COVID-19 Tracker'),
        html.Div(
            dcc.Dropdown(
                id='dropdown',
                options=['Positive Cases', 'Negative Cases', 'Deaths', 'Cumulative Hospitalizations',
                         'Total Test Results', 'Cumulative ICU', 'Cumulative Ventilator'],
                value='Positive Cases'
            )
        ),
        dcc.Graph(
            id='covid-graph',
            figure=px.bar(df, x='date', y='positive', labels={'positive': 'Positive Cases'})
        )
    ]
)

# The callback updates the graph depending on the selected value within the dropdown bar
@app.callback(
    Output(component_id='covid-graph', component_property='figure'),
    Input(component_id='dropdown', component_property='value')
)
def graph_changer(value):
    """
    This function is used for the callback that updates the graph depending on what value is selected in the dropdown
    :param value:
    :return:
    """
    if value == 'Positive Cases':
        return graph_generator('positive')
    elif value == 'Negative Cases':
        return graph_generator('negative')
    elif value == 'Deaths':
        return graph_generator('death')
    elif value == 'Cumulative Hospitalizations':
        return graph_generator('hospitalizedCumulative')
    elif value == 'Total Test Results':
        return graph_generator('totalTestResults')
    elif value == 'Cumulative ICU':
        return graph_generator('inIcuCumulative')
    elif value == 'Cumulative Ventilator':
        return graph_generator('onVentilatorCumulative')
    else:
        raise exceptions.PreventUpdate


# Initializes dash app
if __name__ == '__main__':
    app.run_server(debug=True)
