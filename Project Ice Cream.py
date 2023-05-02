""" 
Project.py is an Ice cream shop assistant that helps a cashier take an order
"""

#Variable that holds the total cost of the order
totalcost = 0
#Boolean that determians if the order is complete
order_status = False

print("")
print("Welcome to the Ice Cream shop!")
print("")

#Main function
def order():
    #Allows the totalcost and order_status to be edited from inside the function
    global totalcost
    global order_status
    
    #Ask the user for what size they want
    size = input("Would you like a single or double scoop?: ")
    #Tells the user their input is invalid and ask for a new response
    while size != "single" and size != "double":
        print("That is not a valid size! Please pick either single or double")
        size = input("Would you like a single or double cone?: ")
    if size == "single":
        #Single cost
        totalcost = totalcost + 5.00
    else:
        #Double cost
        totalcost = totalcost + 9.00


    #Ask the user for what type of cone they want
    cone = input("Would you like a regular cone or waffle cone?: ")
    #Tells the user their input is invalid and ask for a new response
    while cone != "regular" and cone != "waffle":
        print("That is not a valid type! Please pick either regular or waffle")
        cone = input("Would you like a regular cone or waffle cone?: ")
    if cone == "waffle":
        if size =="single":
            #Cost for a waffle cone with a single scoop
            totalcost = totalcost + 1.00
        else:
            #Cost for a waffle cone with a double scoop
            totalcost = totalcost + 2.00


    #Ask the user if they want flakes
    flakes = input("Would you like flakes on it? (yes or no): ")
    #Tells the user their input is invalid and ask for a new response
    while flakes != "yes" and flakes != "no":
        print("That is not a valid answer! Please pick either yes or no")
        flakes = input("Would you like flakes on it? (yes or no): ")
    flakes_bool = flakes == "yes"
    if flakes_bool:
        #Ask how many flakes the user wants
        flakes_amount = int(input("How many flakes would you like? (1-4): "))
        #Tells the user their input is invalid and ask for a new response
        while flakes_amount < 1 or flakes_amount > 4:
            print("That is not a valid amount! Please pick a new amount")
            flakes_amount = int(input("How many flakes would you like? (1-4): "))
        #Cost of the amount of flakes the user wants 
        totalcost = totalcost + (2.00 * flakes_amount)
        flakes_bool = "Yes"
    else:
        flakes_bool = "No"


    #Ask the user if they want sauce
    sauce = input("Would you like Sauce on it? (yes or no): ")
    #Tells the user their input is invalid and ask for a new response
    while sauce != "yes" and sauce != "no":
        print("That is not a valid answer! Please pick either yes or no")
        sauce = input("Would you like Sauce on it? (yes or no): ")
    sauce_bool = sauce == "yes"
    if sauce_bool:
        #Ask what type of sauce they want
        sauce_type = input("Would you like strawberry, chocolate or both?: ")
        #Tells the user their input is invalid and ask for a new response
        while sauce_type != "strawberry" and sauce_type != "chocolate" and sauce_type != "both":
            print("That is not a valid type! Please pick either strawberry, chocolate, or both")
            sauce_type = input("Would you like strawberry, chocolate or both?: ")
        if sauce_type == "strawberry" or sauce_type == "chocolate":
            totalcost = totalcost + 0.25
        else:
            totalcost = totalcost + 0.5
        sauce_bool = "Yes"
    else:
        sauce_bool = "No"


    #Ask the user if they want chocolate chips
    chips = input("Would you like Chocolate Chips on it? (yes or no): ")
    #Tells the user their input is invalid and ask for a new response
    while chips != "yes" and chips != "no":
        print("That is not a valid answer! Please pick either yes or no")
        chips = input("Would you like Chocolate Chips on it? (yes or no): ")
    chips_bool = chips == "yes"
    if chips_bool:
        totalcost = totalcost + 0.5
        chips_bool = "Yes"
    else:
        chips_bool = "No"


    #Ask the user if they want sprinkles
    sprinkles = input("Would you like Sprinkles on it? (yes or no): ")
    #Tells the user their input is invalid and ask for a new response
    while sprinkles != "yes" and sprinkles != "no":
        print("That is not a valid answer! Please pick either yes or no")
        sprinkles = input("Would you like Sprinkles on it? (yes or no): ")
    sprinkles_bool = sprinkles == "yes"
    if sprinkles_bool:
        totalcost = totalcost + 0.25
        sprinkles_bool = "Yes"
    else:
        sprinkles_bool = "No"

    #Ask the user if they want gummy bears or m&ms
    topping = input("Would you like Gummy Bears or M&Ms on it? (yes or no): ")
    #Tells the user their input is invalid and ask for a new response
    while topping != "yes" and topping != "no":
        print("That is not a valid answer! Please pick either yes or no")
        topping = input("Would you like gummy bears or m&ms on it? (yes or no): ")
    topping_bool = topping == "yes"
    if topping_bool:
        #Ask what type of topping they want
        topping_type = input("Would you like gummy bears, or m&ms? ")
        #Tells the user their input is invalid and ask for a new response
        while topping_type != "gummy bears" and topping_type != "m&ms":
            print("That is not a valid type! Please pick either gummy bears or m&ms")
            topping_type = input("Would you like Gummy Bears, or M&Ms? ")
        topping_size = input("Would you like the single or double size?: ")
        #Tells the user their input is invalid and ask for a new response
        while topping_size != "single" and topping_size != "double":
            print("That is not a valid size! Please pick either single or double")
            topping_size = input("Would you like a single or double size of the toppings?: ")
        if topping_size == "single":
            totalcost = totalcost + 1.00
        else:
            totalcost = totalcost + 2.00
        topping_bool = "Yes"
    else:
        topping_bool = "No"

    #Ask the user if they would like a spoon with their ice cream
    spoon = input("Would you like a spoon with it? (yes or no): ")
    #Tells the user their input is invalid and ask for a new response
    while spoon != "yes" and spoon != "no":
        print("That is not a valid answer! Please pick either yes or no")
        spoon = input("Would you like a spoon with it? (yes or no): ")
    spoon_bool = spoon == "yes"
    if spoon_bool:
        totalcost = totalcost + 1.5
        spoon_bool = "Yes"
    else:
        spoon_bool = "No"

    #Ask the user if they want another ice cream
    order_another = input("Would you like to make another Ice cream order?: ")
    #Tells the user their input is invalid and ask for a new response
    while order_another != "yes" and order_another != "no":
        print("That is not a valid answer! Please pick either yes or no")
        order_another = input("Would you like to make another Ice cream order?: ")
    order_bool = order_another == "yes"
    if order_bool:
        order_status = False
        print("")
    else:
        order_status = True

while order_status == False:
    order()

print("")
print("*********************")
print("Order: ")
print("")
print("Total: $" + str(totalcost))
print("*********************")
print("")

change = float(input("How much money did the customer pay? (How much did they hand the cashier): "))
#Tells the user their input is invalid and ask for a new response
while change < 0:
    print("They cannot pay with a negitive amount!")
    change = float(input("How much money did the customer pay? (How much did they hand the cashier): "))
change_math = change
change_math = change_math - totalcost
if change_math < 0:
    print("")
    print("The customer did not pay enough to cover the cost of the order")
    print("They owe: $" + str(change_math * -1))
else:
    print("You give $" + str(change_math) + " back to the customer")

print("")
review = input("Have a nice day!")