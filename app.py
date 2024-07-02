import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    "Tariff": ["AGILE-24-04-03", "AGILE-BB-24-04-03", "COOP-FIX-12M-24-06-28", "COOP-PP-VAR-20-04-01"],
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
    html.Button('Connect Your Supplier', id='submit-val', n_clicks=0),
    dcc.Dropdown(
        id='tariff-dropdown',
        options=[
            {'label': 'AGILE-24-04-03', 'value': 'AGILE-24-04-03'},
            {'label': 'AGILE-BB-24-04-03', 'value': 'AGILE-BB-24-04-03'},
            {'label': 'COOP-FIX-12M-24-06-28', 'value': 'COOP-FIX-12M-24-06-28'},
            {'label': 'COOP-PP-VAR-20-04-01', 'value': 'COOP-PP-VAR-20-04-01'}
        ],
        value='AGILE-24-04-03'
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
    ),
    dcc.Graph(id='bar-chart'),
    dcc.Graph(id='line-chart'),
    html.Div(id='cost-saving')
])

# Define callback to update the bar chart based on the dropdown selection
@app.callback(
    Output('bar-chart', 'figure'),
    Input('tariff-dropdown', 'value')
)
def update_bar_chart(selected_tariff):
    fig = px.bar(df, x='Tariff', y='Amount', title=f'Amount of {selected_tariff}')
    return fig


# Define callback to update the line chart based on the dropdown selection
@app.callback(
    Output('line-chart', 'figure'),
    Input('tariff-dropdown', 'value')
)
def update_line_chart(selected_tariff):
    fig = px.line(df, x='Tariff', y='Amount', title=f'Energy Cost Per Tariff', markers=True)
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

# Callback to calculate and display cost-saving
@app.callback(
    Output('cost-saving', 'children'),
    Input('tariff-dropdown', 'value'),
    Input('appliance-dropdown', 'value')
)
def update_cost_saving(selected_tariff, selected_appliance):
    if selected_tariff and selected_appliance:
        tariff_amount = df.loc[df['Tariff'] == selected_tariff, 'Amount'].values[0]
        appliance_consumption = appliance_df.loc[appliance_df['Name'] == selected_appliance, 'Consumption'].values[0]
        cost_saving = tariff_amount - appliance_consumption
        return f"Cost Saving for {selected_appliance} under {selected_tariff}: {cost_saving}"
    return "Select both a tariff and an appliance to see cost saving."


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)