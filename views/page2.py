
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
p2Layout = html.Div([
    dbc.Card(
                dbc.CardBody([
            dbc.Row([
                
                dbc.Col([
                    dcc.ConfirmDialog(
                        id='confirm21',
                        message="New Book Succesfully Added",
                    ),
                    dcc.ConfirmDialog(
                        id='confirm22',
                        message="Book Succesfully Edited",
                    ),
                    dcc.ConfirmDialog(
                        id='confirm23',
                        message="Book Succesfully Deleted",
                    ),
                    html.H5('Search By'),
                    dcc.Dropdown(
                        id='criteria2',
                        placeholder='Criteria',
                        options=[
                            {'label': 'bookName', 'value': 'bookName'},
                            {'label': 'authorName', 'value': 'authorName'}
                        ])
                ]),
                dbc.Col([
                    html.Div(id='hidden2', style={'display':'none'}),
                    html.Div(id='hidden21', style={'display':'none'}),
                    html.H5('Search Book'),
                    dbc.Input(
                        id="info2",
                        type='text',
                        placeholder="Key-word",
                    )
                ]),
                dbc.Col(
                    [dbc.Button("Search",id='searchButton2', color="primary", className="mr-1")], style={"float":"right", "padding-top":"15px"}, width=1
                )
            ]),
            dbc.Row(
                dbc.Col([
                    dash_table.DataTable(
                        id='infoTable2',
                        columns=[{"name": i, "id": i} for i in ['bookID', 'bookName', 'authorName', 'typeID', 'publisherName']],
                        page_size=8,
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
],style={'backgroundColor':'#B8D9F4'})
    ),
    html.Hr(),
    dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
        html.H3("Create New Book"),
            dbc.Row([
                dbc.Col([
                    html.H6("Name of the Book"),
                    dbc.Input(
                        id="bookName2",
                        type='text',
                        placeholder="Name of the Book",
                    )
                ]),
                dbc.Col([
                    html.H6('Author of the Book'),
                    dcc.Dropdown(
                        id='bookAuthor2',
                        placeholder='Choose Author')
                ])
            ]),

            dbc.Row([
                dbc.Col([
                    html.H6("Type of the Book"),
                    dcc.Dropdown(
                        id='bookType2',
                        placeholder='Choose Type')
                ]),
                dbc.Col([
                    html.H6("Publisher Of the Book"),
                    dcc.Dropdown(
                        id='bookPublisher2',
                        placeholder='Choose Publisher')
                ])
            ]),
            dbc.Row([dbc.Button("Create", id='addBookButton2', color="primary", className="mr-1")
                ], style={"float":"right", "padding-top":"15px"}
            )
        ]),
        dbc.Col([
            html.H3("Delete or Update Books"),
                    dbc.Row([
                            html.Div(id='hidden22', style={'display': 'none'}),
                            html.Div(id='hidden23', style={'display': 'none'}),
                        dbc.Col([
                            html.H6('Choose Operation'),
                            dcc.Dropdown(
                                id='chooseCRUD2',
                                placeholder='Update or Delete',
                                options=[
                                    {'label': 'DELETE', 'value': 'DELETE'},
                                    {'label': 'UPDATE', 'value': 'UPDATE'}
                                ])
                        ]),
                        dbc.Col([
                            html.H6('Choose BookID'),
                            dcc.Dropdown(
                                id='bookID2',
                                placeholder='BookID')
                        ])
                    ]),

                    html.Hr(),

                    dbc.Row([
                        dbc.Col([
                            html.H6("Edit Name"),
                            dbc.Input(
                                id="newName2",
                                type='text',
                                placeholder="New Name",
                            )
                        ]),
                        dbc.Col([
                            html.H6('Edit authorName'),
                            dcc.Dropdown(
                                id="newAuthorName2",
                                placeholder="New AuthorName",
                            )
                        ])
                    ]),
                    dbc.Row([
                        dbc.Col([
                            html.H6("Edit Publisher"),
                            dcc.Dropdown(
                                id='newPublisher2',
                                placeholder='New Publisher')
                        ]),
                        dbc.Col([
                            html.H6("Edit Type"),
                            dcc.Dropdown(
                                id='newType2',
                                placeholder='New Type',
                                options=[])
                        ])
                    ]),
                    dbc.Row(
                        [dbc.Button("Delete/Update", id='crudButton2', color="warning", className="mr-1")], style={"float": "right", "padding-top": "15px"}
                    )
        ])])],style={'backgroundColor':'#B8D9F4'})
        
    ),dbc.Card(
        dbc.CardBody([
            html.H4('Error messages or Additional Informations: '),
            html.Div(id='output2')
        ])
    ),
    REFRESH_INTERVAL
], style={'background-color': '#FFFFFF'})


