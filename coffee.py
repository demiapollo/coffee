MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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


# Can I write this as a function
def check_resources(menu_item, resource_type):
    """Checking if there is enough resource for the order placed by a user."""
    for resource_type in resources:
        if resources[resource_type] < MENU[menu_item]["ingredients"][resource_type]:
            print(f"Sorry there is not enough {resource_type}")
            return False
        

# return remaining value of resource after processing an order
def remaining_resources(menu_item, resource_type):
    """Updating to reflect remaining resources after processing an order"""
    for resource_type in resources:
        starting_value = resources[resource_type]
        amount_used = MENU[menu_item]["ingredients"][resource_type] 
        resources[resource_type] = starting_value - amount_used
        print(f"{resource_type.title()}: {resources[resource_type]}")


money = 0
keep_working = True
# prompt = input("What would you like? (espresso/latte/cappuccino): ")

while keep_working:
    # Prompt user by asking what they want
    # Prompt should be displayed every time an action has been completed
    prompt = input("What would you like? (espresso/latte/cappuccino): ")

    # Turn off coffee machine with 'off' prompt
    if prompt == "off":
        keep_working = False

    # Print report
    elif prompt == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")

    # Check if resources are sufficient after the user chooses a drink
    else: 
        if check_resources(prompt, resource_type="water") == False:
            keep_working = False
            break        
   
        # Process coins
        # calculate the monetary value of coins inserted
        quarters_inserted = int(input("How many quarters you inserted?: "))
        dimes_inserted = int(input("How many dimes you inserted?: "))  
        nickels_inserted = int(input("How many nickels you inserted?: "))
        pennies_inserted = int(input("How many pennies you inserted? "))     

        total_value_inserted = (quarters_inserted * 0.25) + (dimes_inserted * 0.10) + (nickels_inserted * 0.05) + (pennies_inserted * 0.01)
        
        # Check if the transaction is successful
        if total_value_inserted < MENU[prompt]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
        elif total_value_inserted > MENU[prompt]["cost"]:
            change_returned = total_value_inserted - MENU[prompt]["cost"]
            change_returned = round(change_returned, 2)
            print(f"Here is ${change_returned} dollars in change.")
            money += (MENU[prompt]["cost"])
            # return remaining value of resource after processing an order
            remaining_resources(prompt, resource_type="water")
            print(f"Money: ${money}")
            print(f"Here is your {prompt}. Enjoy!")

