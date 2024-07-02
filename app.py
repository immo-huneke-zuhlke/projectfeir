import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    "Tariff": ["Tariff-1", "Tariff-2", "Tariff-3", "Tariff-4"],
    "Amount": [4, 1, 2, 3]
})

appliance_df = pd.DataFrame({
    "Name": ["Fridge", "Fridge2", "Microwave", "Batterry", "SolarPanel"],
    "Consumption": [4, 3, 1, 2, 3],
    "Type": ["Fridge", "Fridge", "Microwave", "Battery", "SolarPanel"]
})


# Create a Dash app instance
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("FEIR"),
    dcc.Graph(id='bar-chart'),
    dcc.Dropdown(
        id='tariff-dropdown',
        options=[
            {'label': 'Tariff 1', 'value': 'Tariff-1'},
            {'label': 'Tariff 2', 'value': 'Tariff-2'},
            {'label': 'Tariff 3', 'value': 'Tariff-3'},
            {'label': 'Tariff 4', 'value': 'Tariff-4'}
        ],
        value='Tariff-1'
    ),
    dcc.Dropdown(
        id='appliance-type-dropdown',
        options=[
            {'label': 'Fridge', 'value': 'Fridge'},
            {'label': 'Microwave', 'value': 'Microwave'},
            {'label': 'Battery', 'value': 'Battery'},
            {'label': 'SolarPanel', 'value': 'SolarPanel'}
        ],
        value='Fridge'
    ),
    dcc.Dropdown(
        id='appliance-dropdown',
        options=[
            {'label': 'Fridge', 'value': 'Fridge'},
            {'label': 'Microwave', 'value': 'Microwave'},
            {'label': 'Battery', 'value': 'Battery'},
            {'label': 'SolarPanel', 'value': 'SolarPanel'}
        ],
        value='Fridge'
    )
    
])

# Define callback to update the bar chart based on the dropdown selection
@app.callback(
    Output('bar-chart', 'figure'),
    Input('tariff-dropdown', 'value')
)
def update_bar_chart(selected_tariff):
    filtered_df = df[df.Tariff == selected_tariff]
    fig = px.bar(filtered_df, x='Tariff', y='Amount', title=f'Amount of {selected_tariff}')
    return fig

# Callback to update the item dropdown based on category selection
@app.callback(
    Output('appliance-dropdown', 'options'),
    Output('appliance-dropdown', 'value'),
    Input('appliance-type-dropdown', 'value')
)
def set_item_options(selected_category):
    filtered_df = appliance_df[appliance_df.Type == selected_category]
    options = [{'label': item, 'value': item} for item in filtered_df['Name']]
    value = options[0]['value'] if options else None
    return options, value




# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)