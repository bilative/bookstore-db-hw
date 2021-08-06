
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

from datetime import date


REFRESH_INTERVAL = dcc.Interval(
    id='interval-component', interval=4*150005, n_intervals=0)

p4Layout = html.Div([

    dbc.Card([
        dbc.CardBody([
            dbc.Row([
                    dbc.Col([
                        html.H3("Delete Author"),
                        dbc.Row([
                            dbc.Col([
                                html.Div(id='hidden41', style={
                                         'display': 'none'}),
                                dcc.ConfirmDialog(
                                    id='confirm41',
                                    message="Deletion is Succesfull",
                                ),
                                html.H5('Choose Author'),
                                dcc.Dropdown(
                                    id='authorID4',
                                    placeholder='By Name'),
                                html.Hr(),
                                dbc.Button("Delete", id='authorDelete4',
                                           color="danger", className="mr-1")
                            ]),
                            dbc.Col([
                                dash_table.DataTable(
                                    id='authorTable4',
                                    columns=[{"name": i, "id": i} for i in [
                                        'authorID', 'authorName', 'authorBirthDate']],
                                    page_size=3,
                                    style_header={
                                        'backgroundColor': 'rgb(30, 30, 30)', 'fontWeight': 'bold', 'color': 'white'
                                    })
                            ])
                        ])
                    ]),
                    dbc.Col([
                        html.H3("Add Author If No Exist"),
                        dbc.Row([

                            html.Div([
                                dbc.Input(
                                    id="newAuthor41",
                                    type='text',
                                    placeholder="Customer Name Search",
                                )], style={"width": "70%", 'margin-left': '30px'}),
                            html.Div([
                                dbc.Input(
                                    id="authorDate40",
                                    type='text',
                                    placeholder="Write yyyy-mm-dd as digit",
                                )], style={"width": "70%", 'margin-left': '30px'}),
                            html.Hr(),
                            dbc.Button("Save", id='addAuthor42',
                                       color="info", className="mr-1")

                        ])
                    ])
                    ])
        ], style={'backgroundColor': '#B8D9F4'}),
    ]),

    dbc.Card([
        dbc.CardBody([
            dbc.Row([
                    dbc.Col([
                        html.H3("Delete Publisher"),
                        dbc.Row([
                            dbc.Col([
                                dcc.ConfirmDialog(
                                    id='confirm42',
                                    message="New Customer Succesfully Added",
                                ),
                                html.H5('Choose Publisher'),
                                dcc.Dropdown(
                                    id='publisherID4',
                                    placeholder='By Publisher'),
                                html.Hr(),
                                dbc.Button("Delete", id='publisherDelete4',
                                           color="danger", className="mr-1")
                            ]),
                            dbc.Col([
                                dash_table.DataTable(
                                    id='publisherTable4',
                                    columns=[{"name": i, "id": i} for i in [
                                        'publisherID', 'publisherName']],
                                    page_size=3,
                                    style_header={
                                        'backgroundColor': 'rgb(30, 30, 30)', 'fontWeight': 'bold', 'color': 'white'
                                    })
                            ])
                        ])
                    ]),
                    dbc.Col([
                        html.H3("Add Publisher If Not Exist"),
                        dbc.Row([

                            html.Div([dbc.Input(
                                id="newPublisher41",
                                type='text',
                                placeholder="Name of new Publisher",
                            )], style={"width": "70%", 'margin-left': '30px'}),
                            html.Hr(),
                            dbc.Button("Save", id='addPublisher42',
                                       color="info", className="mr-1")

                        ])
                    ])
                    ])
        ], style={'backgroundColor': '#CABACA'}),
    ]),


    dbc.Card([
        dbc.CardBody([
            dbc.Row([
                    dbc.Col([
                        html.H3("Delete Book Type"),
                        dbc.Row([
                            dbc.Col([
                                dcc.ConfirmDialog(
                                    id='confirm43',
                                    message="New Customer Succesfully Added",
                                ),
                                html.H5('Choose Type'),
                                dcc.Dropdown(
                                    id='typeID4',
                                    placeholder='By Name'),
                                html.Hr(),
                                dbc.Button("Delete", id='typeDelete4',
                                           color="danger", className="mr-1")
                            ]),
                            dbc.Col([
                                dash_table.DataTable(
                                    id='typeTable4',
                                    columns=[{"name": i, "id": i}
                                             for i in ['typeID', 'typeName']],
                                    page_size=3,
                                    style_header={
                                        'backgroundColor': 'rgb(30, 30, 30)', 'fontWeight': 'bold', 'color': 'white'
                                    })
                            ])
                        ])
                    ]),
                    dbc.Col([
                        html.H3("Add Type If Not Exist"),
                        dbc.Row([

                            html.Div([dbc.Input(
                                id="newType41",
                                type='text',
                                placeholder="New Book Type?",
                            )], style={"width": "70%", 'margin-left': '30px'}),
                            html.Hr(),
                            dbc.Button("Save", id='addType42',
                                       color="info", className="mr-1")

                        ])
                    ])
                    ])
        ], style={'backgroundColor': '#F4D35E'}),
    ]),


    dbc.Card([
        dbc.CardBody([
            dbc.Row([
                    dbc.Col([
                        html.H3("Delete Branch"),
                        dbc.Row([
                            dbc.Col([
                                dcc.ConfirmDialog(
                                    id='confirm3',
                                    message="New Branch Succesfully Added",
                                ),
                                html.H5('Choose Branch'),
                                dcc.Dropdown(
                                    id='branchID4',
                                    placeholder='By Name'),
                                html.Hr(),
                                dbc.Button("Delete", id='branchDelete4',
                                           color="danger", className="mr-1")
                            ]),
                            dbc.Col([
                                dash_table.DataTable(
                                    id='branchTable4',
                                    columns=[{"name": i, "id": i} for i in [
                                        'branchID', 'branchName', 'cityID']],
                                    page_size=3,
                                    style_header={
                                        'backgroundColor': 'rgb(30, 30, 30)', 'fontWeight': 'bold', 'color': 'white'
                                    })
                            ])
                        ])
                    ]),
                    dbc.Col([
                        html.H3("Add Branch If Not Exist"),
                        dbc.Row([

                            html.Div([
                                dbc.Input(
                                    id="newBranch41",
                                    type='text',
                                    placeholder="New BranchName",
                                ),

                                dcc.Dropdown(
                                    id='branchCity40',
                                    placeholder='City'),
                            ], style={"width": "70%", 'margin-left': '30px'}),
                            html.Hr(),
                            dbc.Button("Save", id='addBranch42', color="info", className="mr-1")

                        ])
                    ])
                    ])
        ], style={'backgroundColor': '#EE964B'}),
    ]), dbc.Card(
        dbc.CardBody([
            html.H4('Error messages or Additional Informations: '),
            html.Div(id='output4')
        ])
    ),

    REFRESH_INTERVAL
], style={'background-color': '#FFFFFF'})
