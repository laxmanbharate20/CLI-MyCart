from os import system, name
import admin
import customer

stock = {}
if name == 'nt':
    _ = system('cls')
else:
    _ = system('clear')

stock = admin.signin()
if name == 'nt':
    _ = system('cls')
else:
    _ = system('clear')
customer.stock = stock
customer.signin()
print("Do You Want To Shop Again(y/n)")
choice = input()
if choice == 'Y' or choice == 'y':
    customer.stock = stock
    customer.signin()
else:
    pass
