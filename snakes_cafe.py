# create and print menu

menu = """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                  **
** To quit at any time, type "quit" **
** Type "options" to see commands.  **
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
    total_items = order_summary
    top_bottom_lines = "*"*(len(str(total_items))+2)
    print(f"""
            {top_bottom_lines}
            *{summ.center(len(str(total_items)))}*         
            *{str(total_items).center(1)}*    
            {top_bottom_lines}
    """)


#acknowledge order
def show_order(order):
  
  if menu_items[order] == 1:
    print(f"\n** {menu_items[order]} {order} has been added to your meal **\n")
  else:
    print(f"\n** {menu_items[order]} {order}s have been added to your meal **\n")   
  
  take_order()

def update_order_num(order):
  menu_items[order] += 1
  order_summary[order] = menu_items[order]


def take_order():
  meal_order = input('> ')
  if meal_order == 'quit':
      print('\nGoodbye!\n')
      quit()
  
  if meal_order == 'menu':
      print(menu)
      take_order()

  if meal_order == 'summary':
      print(show_summary())
      take_order()

  if meal_order == 'options':
      print(show_commands())
      take_order()

  if meal_order in menu_items:
    update_order_num(meal_order)
    show_order(meal_order)
    
  else: 
    print("\nItem Not Found\n")

def show_commands():
    print("Command Options: menu | summary | quit ")

# call functions
print_menu()
take_order()
# show_summary()