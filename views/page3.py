
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

p3Layout = html.Div([

    dbc.Card([
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    dcc.ConfirmDialog(
                        id='confirm3',
                        message="New Customer Succesfully Added",
                    ),
                    html.H5('Search By'),
                    dcc.Dropdown(
                        id='criteria3',
                        placeholder='Name or phoneNumber',
                        options=[
                            {'label': 'phoneNumber', 'value': 'phoneNumber'},
                            {'label': 'customerID', 'value': 'customerID'}
                        ], value='customerID')
                ]),
                dbc.Col([
                    html.Div(id='hidden31', style={'display': 'none'}),
                    html.Div(id='hidden32', style={'display': 'none'}),
                    html.H5('Choose Info'),
                    dcc.Dropdown(
                        id="info3",
                        placeholder="Customer Name Search",
                    )
                ]),
                dbc.Col(
                    [dbc.Button("search", id='searchButton3', color="primary", className="mr-1")], style={"float": "right", "padding-top": "15px"}, width=1
                ),
                dbc.Col([
                    html.H5('Information of Choosen Customer'),
                    dash_table.DataTable(
                        id='infoTable3',
                        columns=[{"name": i, "id": i} for i in ['customerName', 'customerSurname',
                                                                'customerID', 'townName', 'phoneNumber']],
                        page_size=3,
                        style_header={
                            'backgroundColor': 'rgb(30, 30, 30)', 'fontWeight': 'bold'
                        },
                        style_cell={
                            'backgroundColor': 'rgb(50,50,50)',
                            'color':'white',
                            'whiteSpace':'normal',
                            'overflow': 'hidden',
                            'textOverflow': 'ellipsis',
                            'minWidth': '130px', 'width': '130px', 'maxWidth': '130px'
                        })
                ]),
            ]),
            dbc.Row(
                dbc.Col([
                    html.H4("Choosen Customer's Transactions"),
                    dash_table.DataTable(
                        id='custTranTable3',
                        columns=[{"name": i, "id": i} for i in ['date', 'customerName',
                                                                'bookName', 'branchName', 'count', 'price']],
                        page_size=6,
                        style_header={
                            'backgroundColor': 'rgb(30, 30, 30)', 'fontWeight': 'bold'
                        },
                        style_cell={
                            'backgroundColor': 'rgb(50,50,50)',
                            'color':'white',
                            'whiteSpace':'normal',
                            'overflow': 'hidden',
                            'textOverflow': 'ellipsis',
                            'minWidth': '130px', 'width': '130px', 'maxWidth': '130px'
                        })
                ], style={"height": "300px"})
            )
        ])
    ],style={'backgroundColor':'#B8D9F4'}), 
        html.Hr(),
    dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    html.H4("Add New Customer"),
                    dbc.Row([
                        dbc.Col([
                            html.H5("Customer Name"),
                            dbc.Input(
                                id="customerName3",
                                type='text',
                                placeholder="Name",
                            )
                        ]),
                        dbc.Col([
                            html.H5('Customer Surname'),
                            dbc.Input(
                                id="customerSurname3",
                                type='text',
                                placeholder="Surname",
                            )
                        ])
                    ]),

                    dbc.Row([
                        dbc.Col([
                            html.H5("City"),
                            dcc.Dropdown(
                                id='customerCity3',
                                placeholder='City')
                        ]),
                        dbc.Col([
                            html.H5("Town"),
                            dcc.Dropdown(
                                id='customerTown3',
                                placeholder='Town',
                                options=[])
                        ]),
                        dbc.Col([
                            html.H5("Phone Number"),
                            dbc.Input(
                                id="phoneNumber3",
                                type='number',
                                placeholder="xxx-xxx-xx-xx",
                            )
                        ])
                    ]),
                    dbc.Row(
                        [dbc.Button("Save", id='customerSave3', color="primary", className="mr-1")], style={"float": "right", "padding-top": "15px"}
                    )
                ], width=6),


                dbc.Col([
                    html.H4("Delete / Update Customers"),
                    dbc.Row([
                            html.Div(id='hidden33', style={'display': 'none'}),
                        dbc.Col([
                            html.H5('Choose Operation'),
                            dcc.Dropdown(
                                id='chooseCRUD3',
                                placeholder='Delete/Update',
                                options=[
                                    {'label': 'DELETE', 'value': 'DELETE'},
                                    {'label': 'UPDATE', 'value': 'UPDATE'}
                                ])
                        ]),
                        dbc.Col([
                            html.H5('CustomerID'),
                            dcc.Dropdown(
                                id='customerID3',
                                placeholder='customerID')
                        ])
                    ]),

                    html.Hr(),

                    dbc.Row([
                        dbc.Col([
                            html.H5("New Name"),
                            dbc.Input(
                                id="newName3",
                                type='text',
                                placeholder="Name",
                            )
                        ]),
                        dbc.Col([
                            html.H5('New Surname'),
                            dbc.Input(
                                id="newSurname3",
                                type='text',
                                placeholder="Surname",
                            )
                        ])
                    ]),
                    dbc.Row([
                        dbc.Col([
                            html.H5("New City"),
                            dcc.Dropdown(
                                id='newCity3',
                                placeholder='City')
                        ]),
                        dbc.Col([
                            html.H5("New Town"),
                            dcc.Dropdown(
                                id='newTown3',
                                placeholder='Town',
                                options=[])
                        ]),
                        dbc.Col([
                            html.H5("New Phone Number"),
                            dbc.Input(
                                id="newNumber3",
                                type='number',
                                placeholder="xxx-xxx-xx-xx",
                            )
                        ])
                    ]),
                    dbc.Row(
                        [dbc.Button("Delete/Update", id='changeButton3', color="warning", className="mr-1")], style={"float": "right", "padding-top": "15px"}
                    )


                ]),
            ])

        ],style={'backgroundColor':'#B8D9F4'})

    ),dbc.Card(
        dbc.CardBody([
            html.H4('Error messages or Additional Informations: '),
            html.Div(id='output3'),
            html.Div(id='output31')
        ])
    ),
    REFRESH_INTERVAL
], style={'background-color': '#FFFFFF'})
