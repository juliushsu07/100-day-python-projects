import decimal

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# 4 cases: espresso/latte/cappuccino or off.
def process_input(user_input):
    if userInput == "espresso" or userInput == "latte" or userInput == "cappuccino":
        check_resources(userInput)
    elif userInput == "off":
        print("See you next time!")
    elif userInput == "report":
        print(resources)
    else:
        print("Sorry I cannot understand your request!")


def check_resources(coffee_type):
    ingredients = {'water': MENU[coffee_type]['ingredients']['water'],
                   'coffee': MENU[coffee_type]['ingredients']['coffee'],
                   'milk': 0}

    if resources['water'] < ingredients['water']:
        print("Sorry there is not enough water!")
    elif resources['coffee'] < ingredients['coffee']:
        print("Sorry there is not enough coffee!")
    elif coffee_type != "espresso":
        ingredients['milk'] = MENU[coffee_type]['ingredients']['milk']
        if resources['milk'] < ingredients['milk']:
            print("Sorry there is not enough milk!")
        else:
            process_coins(MENU[coffee_type]["cost"], ingredients, coffee_type)
    else:
        process_coins(MENU[coffee_type]["cost"], ingredients, coffee_type)


def process_coins(cost, ingredients, coffee_type):
    sum_of_coins = decimal.Decimal(0.00)
    print(cost)
    quarters = input("how many quarters? ")
    dimes = input("how many dimes? ")
    nickles = input("how many nickles? ")
    pennies = input("how many pennies? ")

    sum_of_coins = 0.25 * int(quarters) + 0.10 * int(dimes) + 0.05 * int(nickles) + 0.01 * int(pennies)
    change = sum_of_coins - cost
    print(sum_of_coins)
    if change < 0:
        print("Sorry that's not enough money. Money refunded.")
    else:
        make_coffee(ingredients, coffee_type)
        print(f"Here is {change} in change.")


# def checkTransaction():
#
def make_coffee(ingredients, coffee_type):
    resources['water'] -= ingredients['water']
    resources['coffee'] -= ingredients['coffee']
    if coffee_type != 'espresso':
        resources['milk'] -= ingredients['milk']
    print(f"Here is your {coffee_type}. Enjoy!")


STATUS = 'ON'

while STATUS == 'ON':
    userInput = input("What would you like? (espresso/latte/cappuccino): ")
    process_input(userInput)
    if userInput == 'off':
        STATUS = 'OFF'
