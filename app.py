import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import warnings
from datetime import date

from libs.inserts import *
from libs.deletes import *
from libs.updates import *
from libs.readDb import *
from libs.buttons import *

from views.page1 import p1Layout
from views.page2 import p2Layout
from views.page3 import p3Layout
from views.page4 import p4Layout
from views.page5 import p5Layout
from views.designDetails import *

warnings.filterwarnings('ignore')


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config.suppress_callback_exceptions = True
content = html.Div(id="page-content", style=CONTENT_STYLE)
app.layout = html.Div(
    [dcc.Location(id="url"), sidebar, content])


##############################################
################# PAGE 1 #####################
##############################################

@app.callback([Output('info1', 'options'),
              Output('branchName1', 'options'),
              Output('deleteTran1', 'options'),
              Output('authorName1', 'options')],
              [Input('infoType1', 'value')])
def fill_transactionDropdowns(typeCustomer_):
    customers = readTable('CUSTOMERTBL')
    if (typeCustomer_ == 'customerID'):
        customerOptions = [{'label': i, 'value': i}
                           for i in list(customers['customerID'])]
    else:
        customerOptions = [{'label': str(i) + " "+str(k) + "-->" + str(j), 'value': j} for i, j, k in zip(
            customers['customerName'], customers['customerID'], customers['customerSurname'])]
    branchs = readTable('BRANCHTBL')
    branchsOptions = [{'label': j, 'value': i} for i, j in zip(
        list(branchs['branchID']), list(branchs['branchName']))]

    author = readTable('authorTBL')
    authorOptions = [{'label': j, 'value': i} for i, j in zip(
        list(author['authorID']), list(author['authorName']))]

    transactions = readTable('transactionTBL')
    transactionsOptions = [{'label': i, 'value': i}
                           for i in transactions['transactionID']]

    return customerOptions, branchsOptions, transactionsOptions, authorOptions


@app.callback(Output('bookName1', 'options'),
              Input('authorName1', 'value'))
def booknames_by_author(authorID_):
    books = readTable('BookTBL')
    books = books[books['authorID'] == authorID_]
    booksOptions = [{'label': j, 'value': i}
                    for i, j in zip(list(books['bookID']), list(books['bookName']))]

    return booksOptions


@app.callback(Output('authTran1', 'data'),
              Input('deleteTran1', 'value'))
def latest_transactions(tranID_):
    transactions = transactionList1()
    df = transactions[transactions['transactionID'] == tranID_]
    return df.to_dict('records')


@app.callback(Output('confirm12', 'displayed'),
              [Input('deleteTran1', 'value'),
              Input('deleteButton1', 'n_clicks')])
def confirm_transaction(tranID_, click_):
    isTrue = BUTTONS['deleteTransaction'].isNew(click_)
    if ((isTrue) & (tranID_ != None)):
        deleteFunc('transactionTBL', 'transactionID', tranID_)
        return True


@app.callback([Output('allTransactions1', 'data'),
               Output('confirm11', 'displayed'),
               Output('output1', 'children')],
              [Input('transactionButton1', 'n_clicks'),
              Input('info1', 'value'),
              Input('branchName1', 'value'),
              Input('bookName1', 'value'),
              Input('tranQuantity1', 'value'),
              Input('price1', 'value')])
def sales_transactions(click_, info1_, branch1_, bookName1_,  quantity_, price1_):
    df = transactionList1()
    isTrue = BUTTONS['addTransaction'].isNew(click_)
    if isTrue:
        if ((info1_ == None) | (bookName1_ == None) | (branch1_ == None) | (quantity_ == None)):
            return df.to_dict('records'), False, "BE CAREFULL!!!/n There is some NULL VALUES"
        try:
            addFunc(table='transactionTBL', listem=[
                    info1_, bookName1_, branch1_, quantity_, price1_])
        except Exception as ex:
            if "Arithmetic overflow error converting" in str(ex):
                return df.to_dict('records'), False, "Price could be max 9999.99!! Change the amount!!"
            return df.to_dict('records'), False, str(ex)
        return df.to_dict('records'), True, "Transaction is successfully completed"
    return df.to_dict('records'), False, "No transaction or error"


##############################################
################# PAGE 2 #####################
##############################################

@app.callback(Output('infoTable2', 'data'),
              [Input('criteria2', 'value'),
              Input('info2', 'value'),
              Input('searchButton2', 'n_clicks')])
def search_books(criteria_, info_, click_):
    isNew = BUTTONS['searchBook'].isNew(click_)
    if isNew:
        if ((info_ == None) & (criteria_ == None)):
            df = tumKitaplar()
            return df.to_dict('records')
        elif criteria_ == "authorName":
            df = searchByAuthor(str(info_))
            return df.to_dict('records')
        else:
            df = search('BOOKTBL', str(criteria_), str(info_))
            return df.to_dict('records')
    df = tumKitaplar()
    return df.to_dict('records')


@app.callback([Output('bookAuthor2', 'options'),
               Output('bookPublisher2', 'options'),
               Output('bookType2', 'options')],
              Input("hidden21", "value"))
def fill_book_dropdowns(hidden21):
    authors = readTable('AUTHORTBL')
    authorOptions = [{'label': s, 'value': id}
                     for s, id in zip(authors['authorName'], authors['authorID'])]

    publishers = readTable('publisherTBL')
    publisherOptions = [{'label': s, 'value': id} for s, id in zip(
        publishers['publisherName'], publishers['publisherID'])]

    types_ = readTable('typeTBL')
    typeOptions = [{'label': i, 'value': j}
                   for i, j in zip(types_['typeName'], types_['typeID'])]

    return authorOptions, publisherOptions, typeOptions


@app.callback([Output('hidden2', 'value'),
               Output('confirm21', 'displayed'),
               Output('output2', 'children')],
              [Input("bookName2", "value"),
              Input("bookAuthor2", "value"),
              Input("bookType2", "value"),
              Input("bookPublisher2", "value"),
              Input('addBookButton2', 'n_clicks')])
def add_new_books(bookName_, authorID_, type_, publisherID_, click_):
    isNew21 = BUTTONS['addBook'].isNew(click_)
    if isNew21:
        if ((bookName_ == None) | (authorID_ == None) | (type_ == None) | (publisherID_ == None)):
            return 0, False, "BE CAREFULL!!!/n There is some NULL VALUES"
        try:
            addFunc(table='bookTBL', listem=[
                    bookName_, authorID_, type_, publisherID_])
        except Exception as ex:
            if "UNIQUE KEY" in str(ex):
                return 0, False, "This Book Allready Added the System!!"
            return 0, False, str(ex)
        return 0, True, "New book Succesfully added the DB!!"
    return 0, False, "No problem"


@app.callback([Output('bookID2', 'options'),
               Output('newAuthorName2', 'options'),
               Output('newPublisher2', 'options'),
               Output('newType2', 'options')],
              Input('hidden22', 'value'))
def fill_book_dropdowns2(click):
    book = readTable('bookTBL')
    bookOpt = [{'label': i, 'value': i} for i in book['bookID']]
    author = readTable('authorTBL')
    authorOpt = [{'label': i, 'value': j}
                 for i, j in zip(author['authorName'], author['authorID'])]

    publisher = readTable('publisherTBL')
    publisherOpt = [{'label': i, 'value': j} for i, j in zip(
        publisher['publisherName'], publisher['publisherID'])]

    type_ = readTable('typeTBL')
    typeOpt = [{'label': i, 'value': j}
               for i, j in zip(type_['typeName'], type_['typeID'])]

    return bookOpt, authorOpt, publisherOpt, typeOpt


@app.callback([Output('confirm22', 'displayed'),
               Output('confirm23', 'displayed')],
              [Input('chooseCRUD2', 'value'),
               Input('bookID2', 'value'),
               Input('newName2', 'value'),
               Input('newAuthorName2', 'value'),
               Input('newPublisher2', 'value'),
               Input('newType2', 'value'),
              Input('crudButton2', 'n_clicks')])
def update_books(CRUD_, bookID_, newName_, newAuthor_, newPublisher_, newType_, click_):
    isTrue = BUTTONS['updateBook'].isNew(click_)
    if isTrue:
        if ((CRUD_ == 'UPDATE') and (bookID_ != None) and ((newName_ != None) or (newAuthor_ != None) or (newPublisher_ != None) or (newType_ != None))):
            try:
                updateTable(table = 'bookTBL', by = 'bookID' , condition = bookID_, bookName = repr(newName_),
                            authorID = newAuthor_,typeID= newType_, publisherID= newPublisher_)
                return True, False
            except Exception as ex:
                message = f"""ERROR: + {str(ex)}"""
                return False, False
        elif ((CRUD_ == 'DELETE') and (bookID_ != None)):
            try:
                deleteFunc('bookTBL', 'bookID', bookID_)
                return False, True
            except Exception as ex:
                message = f"""ERROR: + {str(ex)}"""
                return False, False
        return False, False
    return False, False


##############################################
################# PAGE 3 #####################
##############################################


@app.callback([Output('customerCity3', 'options'),
               Output('newCity3', 'options'),
               Output('info3', 'options')],
              [Input("hidden31", "value"),
              Input("criteria3", "value")])
def fill_customer_dropdowns(hidden31, criteria3):
    cities = readTable('cityTBL')
    citiesOpt = [{'label': s, 'value': id}
                 for s, id in zip(cities['cityName'], cities['cityID'])]

    customers = readTable('customerTBL')
    customersOpt = [{'label': i, 'value': i} for i in customers[criteria3]]
    return citiesOpt, citiesOpt, customersOpt


@app.callback([Output('infoTable3', 'data'),
               Output('custTranTable3', 'data')],
              [Input('criteria3', 'value'),
              Input('info3', 'value'),
              Input('searchButton3', 'n_clicks')])
def customer_search_tables(criteria_, info_, click_):
    isNew31 = BUTTONS['searchCustomer'].isNew(click_)
    if isNew31:
        if ((criteria_ == None) | (info_ == None)):
            df = customerNullSearch3()
        else:
            df = customerSearch3(str(criteria_), info_)
        if df.shape[0] < 1:
            return df.to_dict('records'), None
        transactions = customerTransactions3(df.loc[0, 'customerID'])
        return df.to_dict('records'), transactions.to_dict('records')
    df = customerNullSearch3()
    transactions = customerTransactionsNull3()
    return df.to_dict('records'), transactions.to_dict('records')


@app.callback(Output('customerTown3', 'options'),
              Input('customerCity3', 'value'))
def town_by_city(city_):
    towns = readTable('TOWNTBL')
    townOptions = towns[towns['cityID'] == city_]
    options_ = [{'label': s, 'value': id} for s, id in zip(
        list(townOptions['townName']), list(townOptions['townID']))]
    return options_


@app.callback([Output('hidden32', 'value'),
               Output('confirm3', 'displayed'),
               Output('output3', 'children')],
              [Input('customerName3', 'value'),
              Input('customerSurname3', 'value'),
              Input('customerTown3', 'value'),
              Input('phoneNumber3', 'value'),
              Input('customerSave3', 'n_clicks')
               ])
def add_new_customer(name_, surname_, town_, number_, click_):
    isNew32 = BUTTONS['addCustomer'].isNew(click_)
    if isNew32:
        if ((name_ == None) | (surname_ == None) | (town_ == None) | (number_ == None)):
            return 0, False, "There is some MISSING VALUES!! BE CAREFULL!!"
        try:
            addFunc(table='customerTBL', listem=[
                    name_, surname_, number_, town_])
        except Exception as ex:
            if "UNIQUE KEY" in str(ex):
                return 0, False, "This Customer is Allready Added the System!!"
            elif "chk_phoneNumber" in str(ex):
                return 0, False, "CHECK PHONE NUMBER! Its character lenght is not 10"
            return 0, False, str(ex)
        return 0, True, "New Customer succesfully Added the DB!!"
    return 0, False, " No Problem!!"


@app.callback([Output('customerID3', 'options'),
               Output('newTown3', 'options')],
              [Input('hidden33', 'value'),
               Input('newCity3', 'value')])
def fill_update_customer(click, city_):
    customer = readTable('customerTBL')
    customerID = [{'label': i, 'value': i} for i in customer['customerID']]
    town = readTable('townTBL')
    town = town[town['cityID'] == city_]
    town = [{'label': j, 'value': i}
            for i, j in zip(town['townID'], town['townName'])]
    return customerID, town


@app.callback([Output('hidden33', 'value'),
               Output("output31", "children")],
              [Input('chooseCRUD3', 'value'),
               Input('customerID3', 'value'),
               Input('newName3', 'value'),
               Input('newSurname3', 'value'),
               Input('newTown3', 'value'),
               Input('newNumber3', 'value'),
              Input('changeButton3', 'n_clicks')])
def update_customer(CRUD_, customerID_, custName_, custSurname_, custTown_, custNumber_, click_):
    isTrue = BUTTONS['updateCustomer'].isNew(click_)
    if isTrue:
        if ((CRUD_ == 'UPDATE') and (customerID_ != None) and ((custName_ != None) or (custSurname_ != None) or (custTown_ != None) or (custNumber_ != None))):
            try:
                updateTable(table='customerTBL', by='customerID', condition=customerID_,
                            customerName=repr(custName_), customerSurname=repr(custSurname_), townID=custTown_, phoneNumber=custNumber_)
                return 0, "UPDATE/DELETE INFO: Customer info Updated Succesfully"
            except Exception as ex:
                message = f"""UPDATE/DELETE INFO: + {str(ex)}"""
                return 0, message
        elif ((CRUD_ == 'DELETE') and (customerID_ != None)):
            try:
                deleteFunc('customerTBL', 'customerID', customerID_)
                return 0, "UPDATE/DELETE INFO: Customer info Deleted Succesfully"
            except Exception as ex:
                message = f"""UPDATE/DELETE INFO: + {str(ex)}"""
                return 0, message
        return 0, "No action!"
    return 0, 'UPDATE/DELETE INFO: NO PROBLEM'


##############################################
################# PAGE 4 #####################
##############################################


@app.callback([Output('authorID4', 'options'),
               Output('publisherID4', 'options'),
               Output('typeID4', 'options'),
               Output('branchID4', 'options'),
               Output('branchCity40', 'options')],
              Input("authorDelete4", "n_clicks"))
def fill_other_dropdowns(hidden31):
    author = readTable('authorTBL')
    authorOpt = [{'label': j, 'value': i}
                 for i, j in zip(author['authorID'], author['authorName'])]

    publisher = readTable('publisherTBL')
    publisherOpt = [{'label': j, 'value': i} for i, j in zip(
        publisher['publisherID'], publisher['publisherName'])]

    type_ = readTable('typeTBL')
    typeOpt = [{'label': j, 'value': i}
               for i, j in zip(type_['typeID'], type_['typeName'])]

    branch = readTable('branchTBL')
    branchOpt = [{'label': j, 'value': i}
                 for i, j in zip(branch['branchID'], branch['branchName'])]

    city = readTable('cityTBL')
    cityOpt = [{'label': j, 'value': i}
               for i, j in zip(city['cityID'], city['cityName'])]

    return authorOpt, publisherOpt, typeOpt, branchOpt, cityOpt


@app.callback([Output('authorTable4', 'data'),
               Output('publisherTable4', 'data'),
               Output('typeTable4', 'data'),
               Output('branchTable4', 'data')],
              [Input('authorID4', 'value'),
               Input('publisherID4', 'value'),
               Input('typeID4', 'value'),
               Input('branchID4', 'value')])
def show_others_tables(authorID_, publisherID_, typeID_, branchID_):
    author = readTable('authorTBL').sort_values(by='authorID', ascending=False)
    if authorID_:
        author = author[author['authorID'] == authorID_]
    publisher = readTable('publisherTBL').sort_values(
        by='publisherID', ascending=False)
    if publisherID_:
        publisher = publisher[publisher['publisherID'] == publisherID_]
    type_ = readTable('typeTBL').sort_values(by='typeID', ascending=False)
    if typeID_:
        type_ = type_[type_['typeID'] == typeID_]
    branch = readTable('branchTBL').sort_values(by='branchID', ascending=False)
    if branchID_:
        branch = branch[branch['branchID'] == branchID_]
    return author.to_dict('records'), publisher.to_dict('records'), type_.to_dict('records'), branch.to_dict('records')


@app.callback([Output("confirm41", "displayed"),
               Output("output4", "children")],
              [Input('authorID4', 'value'),
               Input('publisherID4', 'value'),
               Input('typeID4', 'value'),
               Input('branchID4', 'value'),
               Input('authorDelete4', 'n_clicks'),
               Input('publisherDelete4', 'n_clicks'),
               Input('typeDelete4', 'n_clicks'),
               Input('branchDelete4', 'n_clicks')])
def delete_others(authorID_, publisherID_, typeId_, branchID_, click_a, click_p, click_t, click_b):
    nAuthor = BUTTONS['deleteAuthor'].isNew(click_a)
    nPublisher = BUTTONS['deletePublisher'].isNew(click_p)
    nType = BUTTONS['deleteType'].isNew(click_t)
    nBranch = BUTTONS['deleteBranch'].isNew(click_b)

    if ((nAuthor) & (authorID_ != None)):
        try:
            deleteFunc('authorTBL', 'authorID', authorID_)
            return True, f"authorID = {authorID_} was Deleted!"
        except Exception as ex:
            if "The DELETE statement conflicted with the REFERENCE constraint" in str(ex):
                return False, f"FIRSTLY DELETE RELATED BOOKS: ERROR ->The DELETE statement conflicted with the REFERENCE constraint"

    if ((nPublisher) & (publisherID_ != None)):
        try:
            deleteFunc('publisherTBL', 'publisherID', publisherID_)
            return True, f"publisherID = {publisherID_} was Deleted!"
        except Exception as ex:
            if "The DELETE statement conflicted with the REFERENCE constraint" in str(ex):
                return False, f"FIRSTLY DELETE RELATED BOOKS: ERROR ->The DELETE statement conflicted with the REFERENCE constraint"

    if ((nType) & (typeId_ != None)):
        try:
            deleteFunc('typeTBL', 'typeID', typeId_)
            return True, f"typeID = {typeId_} was Deleted!"
        except Exception as ex:
            if "The DELETE statement conflicted with the REFERENCE constraint" in str(ex):
                return False, f"FIRSTLY DELETE RELATED BOOKS: ERROR ->The DELETE statement conflicted with the REFERENCE constraint"

    if ((nBranch) & (branchID_ != None)):
        try:
            deleteFunc('branchTBL', 'branchID', branchID_)
            return True, f"branchID = {branchID_} was Deleted!"
        except Exception as ex:
            if "The DELETE statement conflicted with the REFERENCE constraint" in str(ex):
                return False, f"FIRSTLY DELETE RELATED TRANSACTIONS: ERROR ->The DELETE statement conflicted with the REFERENCE constraint"
    return False, "No action"


@app.callback(Output('hidden41', 'value'),
              [Input('authorDate40', 'value'),
               Input('newAuthor41', 'value'),
               Input('addAuthor42', 'n_clicks'),
               Input('newPublisher41', 'value'),
               Input('addPublisher42', 'n_clicks'),
               Input('newType41', 'value'),
               Input('addType42', 'n_clicks'),
               Input('branchCity40', 'value'),
               Input('newBranch41', 'value'),
               Input('addBranch42', 'n_clicks')])
def update_others(authorDate40, newAuthor41, addAuthor42, newPublisher41, addPublisher42, newType41, addType42, cityBranch40, newBranch41, addBranch42):
    nAuthor = BUTTONS['updateAuthor'].isNew(addAuthor42)
    nPublisher = BUTTONS['updatePublisher'].isNew(addPublisher42)
    nType = BUTTONS['updateType'].isNew(addType42)
    nBranch = BUTTONS['updateBranch'].isNew(addBranch42)

    if ((nAuthor) & (authorDate40 != None) & (newAuthor41 != None)):
        addFunc(table='authorTBL', listem=[newAuthor41, authorDate40])

    if ((nPublisher) & (newPublisher41 != None)):
        addFunc(table='publisherTBL', listem=[newPublisher41])

    if ((nType) & (newType41 != None)):
        addFunc(table='typeTBL', listem=[newType41])

    if ((nBranch) & (newBranch41 != None) & (cityBranch40 != None)):
        addFunc(table='branchTBL', listem=[cityBranch40, newBranch41])
    return 0

##############################################
################# PAGE 5 #####################
##############################################


@app.callback([Output('no1', 'value'),
               Output('no2', 'value'),
               Output('no3', 'value'),
               Output('no4', 'value'),
               Output('no5', 'value'),
               Output('no6', 'value'),
              Output('sunburstChoose5', 'options')],
              Input('interval-component5', 'n_clicks'))
def counter_tables(click):
    no1, no2, no3, no4, no5, no6 = totalNumbers()

    city = readTable('cityTBL')
    cityOpt = [{'label': j, 'value': i}
               for i, j in zip(city['cityName'], city['cityName'])]
    return no1, no2, no3, no4, no5, no6, cityOpt


@app.callback([Output('branchs5', 'figure'),
               Output('sunburst5', 'figure'),
               Output('authorBar5', 'figure')],
              Input('sunburstChoose5', 'value'))
def charts(city_):
    branch_ = priceByBranch()
    branch = px.bar(branch_, x='branchName', y='total price',
                    color='branchName', title="Total Earned Money By branchName (TOP 20)")
    branch.update_layout(paper_bgcolor='#FFF8EB')

    sunBurst_ = branchC(city_)
    sunBurst = px.sunburst(sunBurst_, path=[
                           'city', 'townName', '# of Branch'], values='# of Branch', title=f"# of the Branches in {city_}")
    sunBurst.update_layout(paper_bgcolor='#FFF8EB')

    author_ = AuthorP()
    author = px.bar(author_, x='authorName', y='total price',
                    color='authorName', title="Total Earned Money By Author (TOP 20)")
    author.update_layout(showlegend=False, paper_bgcolor='#FFF8EB')
    return branch, sunBurst, author


@app.callback([Output(f"{i}-link", "active") for i in pageList],
              [Input("url", "pathname")],
              )
def toggle_active_links(pathname):
    if pathname == "/":
        # Treat page 1 as the homepage / index
        return True, False, False, False, False
    return [pathname == f"/{i}" for i in pageList]


@app.callback(Output("page-content", "children"),
              [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/kitap_sorgulama"]:
        return p1Layout
    elif pathname == "/kitap_ekle":
        return p2Layout
    elif pathname == "/musteri":
        return p3Layout
    elif pathname == "/other_tables":
        return p4Layout
    elif pathname == "/summary":
        return p5Layout

    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"This page is not available..."),
        ]
    )


if __name__ == "__main__":
    # app.run_server(debug=True, port=1111)
    app.run_server(debug=True, port=8050, host="0.0.0.0")
