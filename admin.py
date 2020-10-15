from os import system, name

stock = {}


def Choice(i):
    switcher = {
        1: add_product,
        2: update_product,
        3: remove_product,
        4: view_all_product
    }
    switcher.get(i, lambda: 'Invalid')()
    return


def add_product():
    """add product to stock"""
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
    article = input("Enter product name to add:\n")
    if article in stock:
        print("Product already added, please add other product")
    else:
        price = float(input("Enter price of product:\n"))
        stock[article] = price
        print("Product Added successfully.")
    print("Do you wish to add more product? (y/n)")
    c = input()
    if c == 'Y' or c == 'y':
        add_product()
    else:
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')
        return


def remove_product():
    """remove existing product"""
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
    article = input("Enter product name to remove:\n")
    if article in stock:
        del stock[article]
    else:
        print("Given product not exit in stock")
    print("Do you wish to remove any other product (y/n):")
    c = input()
    if c == 'Y' or c == 'y':
        remove_product()
    else:
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')
        return


def update_product():
    """update existing product"""
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
    print("Enter product name to update:\n")
    article = input()
    if article in stock:
        price = float(input("Enter new price of product:\n"))
        stock[article] = price
        print("Price Updated")
    else:
        print("Given product not exit in stock")
    print("Do you wish to update any other product (y/n)")
    c = input()
    if c == 'Y' or c == 'y':
        update_product()
    else:
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')
        return


def view_all_product():
    """ Disply all product"""
    if name == 'nt':
        _ = system('cls')  # for window
    else:
        _ = system('clear')  # for mac and linux
    print("_" * 54)
    print("|", " " * 9, "PRODUCT NAME", " " * 8, "|", " " * 8, "PRICE", " " * 9, "|")
    print("-" * 54)
    for key, values in stock.items():
        print("|", " " * (9 - (len(key) // 2)), key, " " * (8 - (len(key) // 2) + 3), "|",
              " " * (8 - (len(str(values)) // 2) + 3), values, " " * (9 - (len(str(values)) // 2) + 2), "|")
    print("-" * 54)
    return


def logout():
    """Logout the admin panel"""
    print("Logout from admin Panel")
    return


def signin():
    """Admin login and function controlling block"""
    print(
        "Welcome to Admin Panel\n1. To add product\n2. To update product\n3. To remove product\n4. To view all product\n5. To logout")
    choice = int(input().strip())
    while choice < 5:
        Choice(choice)
        print("1. To add product\n2. To update product\n3. To remove product\n4. To view all product\n5. To logout")
        choice = int(input().strip())
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')
    logout()
    return stock
