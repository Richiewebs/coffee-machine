from stuffs import MENU, resources
start_machine = True
change = 0
amount_paid = 0
amount = 0

water_cap = MENU['cappuccino']['ingredients']['water']
milk_cap = MENU['cappuccino']['ingredients']['milk']
coffee_cap = MENU['cappuccino']['ingredients']['coffee']
cost_cap = MENU['cappuccino']['cost']

water_ex = MENU['espresso']['ingredients']['water']

coffee_ex = MENU['espresso']['ingredients']['coffee']
cost_ex = MENU['espresso']['cost']

water_la = MENU['latte']['ingredients']['water']
milk_la = MENU['latte']['ingredients']['milk']
coffee_la = MENU['latte']['ingredients']['coffee']
cost_la = MENU['latte']['cost']

while start_machine:
    request = input("What would you like? (espresso, latte or cappuccino): ")
    if request == "report":
        print(f"Water:{resources['water']}ml")
        print(f"Milk:{resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}g")
        print(f"Money:${amount}")

    elif request == "espresso":
        if water_ex > resources['water']:
            print("Sorry, there's not enough water")
        elif coffee_ex > resources['coffee']:
            print("Sorry there's not enough coffee")
        else:
            print("Please insert coins")
            quarter = int(input("How many quarter"))
            dime = int(input("How many dime"))
            nickel = int(input("How many nickel"))
            penny = int(input("How many penny"))

            amount_paid = (0.25 * quarter) + (0.10 * dime) + (0.05 * nickel) + (0.01 * penny)
            if amount_paid > cost_ex:
                change = round(amount_paid - cost_ex, 2)
                amount += cost_ex
                resources['coffee'] -= coffee_ex
                resources['water'] -= water_ex
                print(f"Your change is ${change}")
                print(f"Enjoy your cup of espresso coffee")
            elif amount_paid < cost_ex:
                print("Not enough funds! Here is your refund")
            else:
                print(f"Enjoy your cup of espresso coffee")

    elif request == "latte":
        if water_la > resources['water']:
            print("Sorry, there's not enough water")
        elif coffee_la > resources['coffee']:
            print("Sorry there's not enough coffee")
        elif milk_la > resources['milk']:
            print("Sorry there's not enough coffee")
        else:
            print("Please insert coins")
            quarter = int(input("How many quarter"))
            dime = int(input("How many dime"))
            nickel = int(input("How many nickel"))
            penny = int(input("How many penny"))

            amount_paid = (0.25 * quarter) + (0.10 * dime) + (0.05 * nickel) + (0.01 * penny)
            if amount_paid > cost_la:
                change = round(amount_paid - cost_la, 2)
                amount += cost_la
                resources['milk'] -= milk_la
                resources['coffee'] -= coffee_la
                resources['water'] -= water_la
                print(f"Your change is ${change}")
                print(f"Enjoy your cup of latte coffee")
            elif amount_paid < cost_la:
                print("Not enough funds! Here is your refund")
            else:
                print(f"Enjoy your latte coffee")

    elif request == "cappuccino":
        if water_cap > resources['water']:
            print("Sorry, there's not enough water")
        elif coffee_cap > resources['coffee']:
            print("Sorry there's not enough coffee")
        elif milk_cap > resources['milk']:
            print("Sorry there's not enough coffee")
        else:
            print("Please insert coins")
            quarter = int(input("How many quarter"))
            dime = int(input("How many dime"))
            nickel = int(input("How many nickel"))
            penny = int(input("How many penny"))

            amount_paid = (0.25 * quarter) + (0.10 * dime) + (0.05 * nickel) + (0.01 * penny)
            if amount_paid > cost_cap:
                change = round(amount_paid - cost_cap, 2)
                amount += cost_cap
                resources['milk'] -= milk_cap
                resources['coffee'] -= coffee_cap
                resources['water'] -= water_cap
                print(f"Your change is ${change}")
                print(f"Enjoy your cup of capuccino coffee")
            elif amount_paid < cost_cap:
                print("Not enough funds! Here is your refund")
            else:
                print(f"Enjoy your cup of capuccino coffee")

    elif request == "off":
        start_machine = False
