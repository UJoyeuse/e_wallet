#!/usr/bin/python3

from order_management import (
    UserManagement,
    Stock,
    Cart,
    Wrapper,
    Menu,
    BookRecords
)

if __name__ == '__main__':
    # files path declaration
    credentials_file = 'data/credentials.txt'
    stock_file = 'data/products.json'
    sales_file = 'data/sales.json'
    prescription_file = 'data/prescriptions.json'

    # load the user management file
    profiles = UserManagement.load(credentials_file)

    # get the logged in user
    pharmacist = profiles.get_logged_in_user()
    # make sure the logged in user is a pharmacist/salesperson
    assert pharmacist.role == 'salesperson', 'You are not allowed to access this feature.'

    # load the resources that we need
    stock = Stock.load(stock_file)
    cart = Cart(stock=stock)

    wrap = Wrapper(stock, pharmacist.username)
    books = BookRecords.load(sales_file)

    # create an instance of the menu
    menu = Menu(stock, profiles, pharmacist, sales_file, prescription_file, stock_file)

    # TODO: Using a while loop, show the menu to the user and guide them through the app