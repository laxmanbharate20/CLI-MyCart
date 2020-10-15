from os import system, name
import time

basket = {}
stock = {}


def Choice(i):
    switcher = {
        1: view_basket,
        2: view_stock,
        3: add_product,
        4: search_in_stock,
        5: remove_from_basket,
        6: display_invoice
    }
    switcher.get(i, lambda: 'Invalid')()
    return


def view_basket():
    """display all products present in basket"""
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
    if (len(basket) == 0):
        print("Basket is empty")
        return
    print("_" * 70)
    print("|", " " * 9, "PRODUCT NAME", " " * 8, "|", " " * 7, "QUANTITY", " " * 7, "|")
    print("-" * 70)
    for key, values in basket.items():
        print("|", " " * (9 - (len(key) // 2)), key, " " * (8 - (len(key) // 2) + 3), "|",
              " " * (7 - (len(str(values[1])) // 2) + 3), values[1], " " * (7 - (len(str(values[1])) // 2) + 2), "|")
    print("-" * 70)
    return


def view_stock():
    """display all products present in stock"""
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
    print("_" * 54)
    print("|", " " * 9, "PRODUCT NAME", " " * 8, "|", " " * 8, "PRICE", " " * 9, "|")
    print("-" * 54)
    for key, values in stock.items():
        print("|", " " * (9 - (len(key) // 2)), key, " " * (8 - (len(key) // 2) + 3), "|",
              " " * (8 - (len(str(values)) // 2) + 3), values, " " * (9 - (len(str(values)) // 2) + 2), "|")
    print("-" * 54)
    return


def add_product():
    """ add product to basket"""
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
    article = input("Enter product name to add:\n")
    if article in stock:
        print("Price of product is ", stock[article])
        # print("Do you wish to add more product (y/n)")
        # c=input()
        # if c=='Y' or c=='y':
        quantity = int(input("Enter the quantity:\n"))
        basket[article] = [stock[article], quantity]
    else:
        print("Product not present in stock")
    print('Do you want to add more product (y/n)')
    c = input()
    if c == 'Y' or c == 'y':
        add_product()
    else:
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')
        return


def search_in_stock():
    """Search product in stock"""
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
    article = input("Enter Product Name To Search\n")
    if article in stock:
        print(" Product Found\nPrice Of Product Is ", stock[article])
    else:
        print("Sorry for the inconvenience Product isn't in our inventory")
    print('Do You Want to Search Any Other Product')
    c = input()
    if c == 'Y' or c == 'y':

        search_in_stock()
    else:
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')
        return


def remove_from_basket():
    """remove product from cart"""
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
    article = input("Enter Product Name To Remove\n")
    if article in basket:
        del basket[article]
        print("Product Removed Successfully")
    print('Do You Want to Remove Any Other Product(y/n)')
    c = input()
    if c == 'Y' or c == 'y':
        remove_from_basket()
    else:
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')
        return


def display_invoice():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
    import datetime
    now = datetime.datetime.now()
    print("Generating Invoice Please Wait")
    summ = 0.0
    indisum = []
    for values in basket.values():
        indisum.append(values[0] * values[1])
        summ += values[0] * values[1]
    print("_" * 70)
    print("            INVOICE")
    print("_" * 70)
    print("TIME STAMP:", now)
    print("_" * 70)
    print("|", " " * 9, "ITEM", " " * 8, "|", " " * 7, "PRICE", " " * 7, "|", " " * 7, "QUANTITY", " " * 7, "|",
          " " * 7, "TOTAL", " " * 7, "|")
    print("-" * 70)
    i = 0
    for key, values in basket.items():
        print("|", " " * (9 - (len(key) // 2)), key, " " * (8 - (len(key) // 2) + 3), "|",
              " " * (7 - (len(str(values[0])) // 2) + 3), values[0], " " * (7 - (len(str(values[0])) // 2) + 2), "|",
              " " * (7 - (len(str(values[1])) // 2) + 3), values[1], " " * (7 - (len(str(values[1])) // 2) + 2), "|",
              " " * (7 - (len(str(indisum[i])) // 2) + 3), indisum[i], " " * (7 - (len(str(indisum[i])) // 2) + 2))
        i += 1

    print("GRAND TOTAL", summ)
    time.sleep(5)
    return


def Signout():
    """logout from customer panel"""
    print("Thank you... Visit again...!")
    return


def signin():
    print(
        "Welcome to Customer Panel\n1. To view products in basket\n2. To view products in inventory\n3. To add products in basket"
        "\n4. To search products in inventory\n5. To remove products from basket\n6. To print invoice"
        "\n7. To logout")
    choice = int(input("\n").strip(' '))
    while choice < 7:
        Choice(choice)
        print("1. To view products in basket\n2. To view products in inventory\n3. To add products in basket"
              "\n4. To search products in inventory\n5. To remove products from basket\n6. To print invoice"
              "\n7. To logout")
        choice = int(input("\n").strip(' '))
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')
    Signout()
    return
