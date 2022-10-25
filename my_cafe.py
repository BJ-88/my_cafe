#Greet Customer and get name for order

print("Welcome to Cafe Grande! \n")

name = input("Can I get a name for your order please?\n\n")

#Thank customer by name

print("thank you so much " + name + "!\n\n")

#Give customer menu and take order
drink_menu = "tea $4, coffee $5, latte $5, frappe $8"

food_menu = "sandwich $5, cookie $3, sub $6, burger $8"

#Get customers drink order
drink_order = input("what would you like to order from our drinks menu?\n\n" + drink_menu + "\n\n")

#Get prices for drink orders
drink_price = 0

if drink_order == "tea":
    drink_price = 4
elif drink_order == "coffee":
    drink_price = 5
elif drink_order == "latte":
    drink_price = 5
elif drink_order == "frappe":
    drink_price = 8
print("OK 1 " + drink_order + " That's $" + str(drink_price))
#Get customers food order
food_order = input("what would you like to order from our food menu?\n\n" + food_menu + "\n\n")
#If customer only wants a drink, repeat drink order and give price. Repeat customers name.
if food_order == "nothing":
  print("OK so just the " + drink_order + ". That'll be $" + str(drink_price) + ". I'll be right back with your " + drink_order + " " + name)
  exit()

#Get prices for food orders
food_price = 0

if food_order == "sandwich":
    food_price = 5
elif food_order == "cookie":
    food_price = 3
elif food_order == "sub":
    food_price = 6
elif food_order == "burger":
    food_price = 8

print("and 1 " + food_order + " That'll be $" + str(food_price))
#Repeat customers full order
print("OK great! so that was a " + food_order + " and a " + drink_order + "\n\n")

#Give customer total price for food and drink
total_price = food_price + drink_price 
#Convert int() data type to str()
#Repeat customers name, full order and give total price
print("Thanks " + name + ". That brings your total to $" + str(total_price) + ". I'll be right back with your " + food_order + " and your " + drink_order + "\n\n")