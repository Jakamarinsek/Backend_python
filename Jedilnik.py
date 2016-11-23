menu = {}
while True:
    food = raw_input("Enter the type of food: ")
    price = raw_input("Enter the price for the food: ")
    menu[food] = price
    new_food = raw_input("Do you want to enter new food (y/n): ").lower()
    if new_food == "n":
        break
menu_file =  open("jedilnik.txt", "w+")
print "Jedilni list: "
menu_file.write("Jedilni list: \n")
for food in menu:
    price = menu[food]
    print food.ljust(8) +"Cena: " + price +"EUR"
    menu_file.write(food.ljust(8) +"Cena: " +price +"EUR \n")
menu_file.close()