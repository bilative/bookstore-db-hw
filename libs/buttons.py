button_aims = ['addBook',
'searchBook',
'updateBook',
'addCustomer',
'searchCustomer',
'updateCustomer',
'addTransaction',
'deleteTransaction',
'deleteAuthor',
'deletePublisher',
'deleteType',
'deleteBranch',
'updateAuthor',
'updatePublisher',
'updateType',
'updateBranch']

class BUTTON:
    def __init__(self, click):
        self.click = click

    def isNew(self, newClick):
        if (self.click == newClick):
            return False
        elif ((newClick == 0) | (newClick == None)):
            return False
        else:
            self.click = newClick
            return True

BUTTONS = {}
for aim in button_aims:
    BUTTONS[aim] = BUTTON(0)
