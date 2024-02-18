from main import MENU


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """ Returns true when order can be made """
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            is_enough = False
            print("Please use code: 'refil' to add some ingredients!")
    return is_enough


def process_coins():
    """ Returns the total calculated from coins inserted """
    print("Pleaase insert coins. ")
    total = int(input("how many quarters? ")) * 0.25
    total += int(input("how many dimes? ")) * 0.1
    total += int(input("how many nickles ")) * 0.05
    total += int(input("how many pennies ")) * 0.01
    return total


def is_transaction_succesful(money_received, drink_cost):
    """Return True if payment is accepted"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deducts the requited ingredients from the resources  """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


is_on = True
profit = 0


while is_on:
    choice = input("What would you like? espresso / latte / cappuccino : ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif choice == "refil":
        for key in resources:
            resources[key] += 500
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_succesful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
