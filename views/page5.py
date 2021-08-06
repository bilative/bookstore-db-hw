
import warnings

import dash
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Button import Button
from dash_bootstrap_components._components.Card import Card
from dash_bootstrap_components._components.CardBody import CardBody
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
import dash_daq as daq
from datetime import date

REFRESH_INTERVAL = dcc.Interval(
    id='interval-component5', interval=4*15005, n_intervals=0)
p5Layout = html.Div([
    dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col(
                    id='card1',
                    children=[
                        html.H6('# of Transaction', style={
                                'font-weight': 'bold'}),
                        daq.LEDDisplay(
                            id='no1',
                            value=0,
                            color='#92e0d3',
                            backgroundColor='#1e2130',
                            size=30
                        )
                    ], width=2
                ),
                dbc.Col(
                    id='card2',
                    children=[
                        html.H6('# of Customer', style={
                                'font-weight': 'bold'}),
                        daq.LEDDisplay(
                            id='no2',
                            value=0,
                            color='#92e0d3',
                            backgroundColor='#1e2130',
                            size=30
                        )
                    ], width=2
                ),
                dbc.Col(
                    id='card3',
                    children=[
                        html.H6('# of Books', style={'font-weight': 'bold'}),
                        daq.LEDDisplay(
                            id='no3',
                            value=0,
                            color='#92e0d3',
                            backgroundColor='#1e2130',
                            size=30
                        )
                    ], width=2
                ),
                dbc.Col(
                    id='card4',
                    children=[
                        html.H6('# of Authors', style={'font-weight': 'bold'}),
                        daq.LEDDisplay(
                            id='no4',
                            value=0,
                            color='#92e0d3',
                            backgroundColor='#1e2130',
                            size=30
                        )
                    ], width=2
                ),
                dbc.Col(
                    id='card5',
                    children=[
                        html.H6('# of Publishers', style={
                                'font-weight': 'bold'}),
                        daq.LEDDisplay(
                            id='no5',
                            value=0,
                            color='#92e0d3',
                            backgroundColor='#1e2130',
                            size=30
                        )
                    ], width=2
                ),
                dbc.Col(
                    id='card6',
                    children=[
                        html.H6('# of Branches', style={
                                'font-weight': 'bold'}),
                        daq.LEDDisplay(
                            id='no6',
                            value=0,
                            color='#92e0d3',
                            backgroundColor='#1e2130',
                            size=30
                        )
                    ], width=2
                )
            ])
        ],style={'backgroundColor':'#B8D9F4'})
    ),
    html.Hr(),
    dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id='branchs5')
                ], width=12)
                ])
        ],style={'backgroundColor':'#B8D9F4'})
    ),
    dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    dcc.Dropdown(
                        id='sunburstChoose5',
                        placeholder='Delete/Update',
                        value='IZMIR'),
                    dcc.Graph(id='sunburst5')
                ],width=5),
                dbc.Col([
                    dcc.Graph(id='authorBar5')
                ],width=7)
                

            ])
        ],style={'backgroundColor':'#B8D9F4'})
    ),

    REFRESH_INTERVAL
], style={'background-color': '#FFFFFF'})
