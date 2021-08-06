
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
p1Layout = html.Div([
    dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    html.H3("Make a Sale"),
                    dbc.Row([
                        
                        dbc.Col([
                            dcc.ConfirmDialog(
                                id='confirm11',
                                message="Sales Transaction Completed Successfully",
                            ),
                            dcc.ConfirmDialog(
                                id='confirm12',
                                message="Transaction Successfully Deleted!",
                            ),
                            html.H5("Search By"),
                            dcc.Dropdown(
                                id='infoType1',
                                placeholder='Search By',
                                options=[
                                    {'label': 'Customer Name','value': 'customerName'},
                                    {'label': 'Customer ID', 'value': 'customerID'}
                                ])
                        ]),
                        dbc.Col([
                            html.Div(id='hidden11', style={'display': 'none'}),
                            html.Div(id='hidden12', style={'display': 'none'}),
                            html.H5('Customer'),
                            dcc.Dropdown(
                                id='info1',
                                placeholder='Choose true customer',
                                optionHeight=80)
                        ]),
                        dbc.Col([
                            html.H5("Branch Name"),
                            dcc.Dropdown(
                                id="branchName1",
                                placeholder="Branch",
                            )
                        ])
                    ]),

                    dbc.Row([
                        dbc.Col([
                            html.H5("Author"),
                            dcc.Dropdown(
                                id='authorName1',
                                placeholder='Author of the Book',
                                optionHeight=80)
                        ]),
                        dbc.Col([
                            html.H5("Book Name"),
                            dcc.Dropdown(
                                id='bookName1',
                                placeholder='Name of the Book',
                                optionHeight=80)
                        ]),
                        dbc.Col([
                            html.H5("Number"),
                            dcc.Dropdown(
                                id='tranQuantity1',
                                placeholder='Count of Book',
                                options=[{'label': i+1, 'value': i+1} for i in range(20)])
                        ]),
                        dbc.Col([
                            html.H5("Price"),
                            dbc.Input(
                                id="price1",
                                type='number',
                                placeholder="digit",
                            )
                        ])
                    ]),
                    dbc.Row(
                        [dbc.Button("Sale", id='transactionButton1', color="primary", className="mr-1")], style={"float": "right", "padding-top": "15px"}
                    )]),
                dbc.Col([
                    
                    html.H3("Delete a Transaction"),
                    html.H5("Transaction ID"),

                    dcc.Dropdown(
                        id='deleteTran1',
                        placeholder='Deletion'),
                    
                    dash_table.DataTable(
                        id='authTran1',
                        columns=[{"name": i, "id": i} for i in [
                            'date','transactionID', 'customerName', 'bookName', 'price']],
                        page_size=10,
                        style_header={
                            'backgroundColor': 'rgb(30, 30, 30)', 'fontWeight': 'bold'
                        },
                        style_cell={
                            'backgroundColor': 'rgb(50,50,50)',
                            'color':'white',
                            'whiteSpace':'normal'
                        }
                    ),
                    html.Div([dbc.Button("Delete Transaction", id='deleteButton1', color="danger", className="mr-1")], style={"float": "right", "padding-top": "15px"})
                ])
            ])],style={'backgroundColor':'#B8D9F4'})

    ),
    html.Hr(),
    dbc.Card(
        dbc.CardBody([
                    html.H3("Previous Transactions"),
            dbc.Row([
                dbc.Col(
                    dash_table.DataTable(
                        id='allTransactions1',
                        columns=[{"name": i, "id": i} for i in [
                            'date', 'transactionID', 'customerName', 'bookName', 'branchName', 'count', 'price']],
                        page_size=10,
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
                        }
                    )
                )
            ])
        ],style={'backgroundColor':'#B8D9F4'})
    ), dbc.Card(
        dbc.CardBody([
            html.H4('Error messages or Additional Informations: '),
            html.Div(id='output1')
        ])
    ),
    REFRESH_INTERVAL
], style={'background-color': '#FFFFFF'})
