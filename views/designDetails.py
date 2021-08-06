
import dash_html_components as html
import dash_bootstrap_components as dbc

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#111111",
    "color": "#C8C8C8"
}


CONTENT_STYLE = {
    "margin-left": "16.5rem",
    "margin-right": "0.5rem",
    "padding": "1rem 0.5rem",
    "bacground-color": "black"
}


pageList = ['kitap_sorgulama', 'kitap_ekle',
            'musteri', "other_tables", 'summary']


sidebar = html.Div(
    [
        html.H2("Bilal's Bookstore", className="display-4"),
        html.Hr(),
        html.P(
            "Sell books, search, check, follow and write queries.", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Transactions", href="/kitap_sorgulama",
                            id="kitap_sorgulama-link"),
                dbc.NavLink("Books", href="/kitap_ekle",
                            id="kitap_ekle-link"),
                dbc.NavLink("Customers",
                            href="/musteri", id="musteri-link"),
                dbc.NavLink("Others",
                            href="/other_tables", id="other_tables-link"),
                dbc.NavLink("Summary",
                            href="/summary", id="summary-link"),
            ],
            vertical=True,
            pills=True,
        )
    ],
    style=SIDEBAR_STYLE,
)