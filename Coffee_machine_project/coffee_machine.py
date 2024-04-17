Menu={
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost":150,
    },
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost":100,
    },
    "cappuccino":{
        "ingredients":
    {
        "water":250,
        "milk":100,
        "coffee":24,
    },
    "cost":200,
    }
}


profit=0
resources = {
    "water":500,
    "milk":200,
    "coffee":100,
}

def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
        return True

is_on=True

while is_on:
    choice=input("What would you like to have? (latte/espresso/cappuccino):")
    if choice=="off":
        is_on=False
    if choice=="report":
        print(f"Water={resources['water']}ml")
        print(f"Milk={resources['milk']}ml")
        print(f"Coffee={resources['coffee']}g")
        print(f"Money=Rs{profit}")
    else:
        coffee_type=Menu[choice]
        print(coffee_type)
        check_resouces(coffee_type['ingredients'])

