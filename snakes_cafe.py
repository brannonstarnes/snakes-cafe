# create and print menu

menu = """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                  **
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
"""

#items on menu, number of orders
menu_items = {
"Wings": 0,
"Cookies": 0,
"Spring Rolls": 0,
"Salmon": 0,
"Steak": 0,
"Meat Tornado": 0,
"A Literal Garden": 0,
"Ice Cream": 0,
"Cake": 0,
"Pie": 0,
"Coffee": 0,
"Tea": 0,
"Unicorn Tears": 0
}

def print_menu():
  print(menu)
  take_order()

#prompt user for order, > with trailing space
meal_order = "Nothing"
order_summary = {}

def show_summary():
    summ = "Order Summary"

    print(f"""
    ***********************************
    **     {summ.center(31)}         ** 
    **{str(order_summary).center(31)}**    
    ***********************************
    """)

#acknowledge order
def show_order(order):
  if menu_items[order] == 1:
    print(f"** {menu_items[order]} {order} has been added to your meal **")
  else:
    print(f"** {menu_items[order]} {order}s have been added to your meal **")   
  take_order()

def update_order_num(order):
  menu_items[order] += 1
#   order_summary[order].append(menu_items[order])


def take_order():
  meal_order = input('> ')
  if meal_order in menu_items:
    update_order_num(meal_order)
    show_order(meal_order)
  else: 
    print("Item Not Found")



# call functions
print_menu()
take_order()