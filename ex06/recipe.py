import sys
import string

def start_program():
    cookbook = {
            "Sandwich" : {
                "ingredients": ["ham", "bread", "cheese", "tomatoes"],
                "meal": "lunch",
                "prep_time": 10
                },
            "Cake" : {
                "ingredients": ["flour", "sugar", "eggs"],
                "meal": "desert",
                "prep_time": 60
                },
            "Salad" : {
                "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
                "meal": "lunch",
                "prep_time": 15
                }
            }
    return cookbook

def print_cookbook(cookbook):
    if len(cookbook) == 0:
        print("Cookbook is empty!")
    else:
        print("Cookbook recipes:")
        for key in cookbook.keys():
            print(key)

def print_recipe(cookbook):
    if len(cookbook) == 0:
        print("Cookbook is empty!")
        return
    print_cookbook(cookbook)
    while True:
        ans = input("Please enter a recipe name to get its details:\n>> ")
        if ans in cookbook.keys():
             print(cookbook[ans])
             break
        else:
            print("Recipe not found in Cookbook!");

def print_program():
    print('''
Welcome to the Python Cookbook!
List of available option:
1: Add a recipe
2: Delete a recipe
3: Print a recipe
4: Print the cookbook
5: Quit
''')

def delete_recipe(cookbook):
    if len(cookbook) == 0:
        print("Cookbook is empty!")
    else:
        print_cookbook(cookbook)
        ans = input("Which recipe do you want to delete?\n>> ")
        removed = cookbook.pop(ans, None)
        if removed != None:
            print(f"Recipe {ans} removed. Say goodbye to it...")
        else:
            print(f"Recipe {ans} not found. Try another time!")

def add_recipe(cookbook):
    name = input("Enter a recipe name:\n>> ")
    if name in cookbook.keys():
        while True:
            ans  = input("Recipe already in cookbook. Do you want to overwrite it? (Yes/No)\n")
            if ans.lower() == "yes":
                break
            elif ans.lower() == "no":
                return
    ingredients = []
    ingredient = input("Enter ingredients:\n>> ")
    while True:
        if ingredient == "":
            break
        ingredients.append(ingredient)
        ingredient = input(">> ")
    meal = input("Enter a meal type:\n>> ")
    while True:
        time = input("Enter preparation time:\n>> ")
        if time.isnumeric():
            time = int(time)
            break
        else:
            print("Preparation time must be a integer number")
    cookbook[name] = {
            "ingredients": ingredients,
            "meal": meal,
            "time": time
            }

if __name__ == "__main__":
    cookbook = start_program()
    is_on = True
    while (is_on):
        print_program()
        ans = input("Please select an option:\n>> ");
        if ans == '1':
            add_recipe(cookbook)
        elif ans == '2':
            delete_recipe(cookbook)
        elif ans == '3':
            print_recipe(cookbook)
        elif ans == '4':
            print_cookbook(cookbook)
        elif ans == '5':
            is_on = False;
        else:
            print("Sorry, this option does not exist.");
