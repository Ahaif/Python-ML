# Part 1: Cookbook and Functions (same as before)

cookbook = {
    "Sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
    },
    "Cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
    },
    "Salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15
    }
}

def print_recipe_names():
    print("Recipe Names:")
    for recipe_name in cookbook:
        print(recipe_name)

def print_recipe_details(recipe_name):
    if recipe_name in cookbook:
        recipe = cookbook[recipe_name]
        print(f"Recipe Name: {recipe_name}")
        print(f"Ingredients: {', '.join(recipe['ingredients'])}")
        print(f"Meal Type: {recipe['meal']}")
        print(f"Preparation Time: {recipe['prep_time']} minutes")
    else:
        print(f"Recipe '{recipe_name}' not found in the cookbook.")

def delete_recipe(recipe_name):
    if recipe_name in cookbook:
        del cookbook[recipe_name]
        print(f"Recipe '{recipe_name}' has been deleted.")
    else:
        print(f"Recipe '{recipe_name}' not found in the cookbook.")

def add_recipe():
    name = input("Enter the recipe name: ")
    ingredients = input("Enter ingredients (comma-separated): ").split(',')
    meal = input("Enter meal type: ")

    prep_time = input("Enter preparation time (minutes): ")
    if prep_time.isdigit() and prep_time:
        prep_time = int(prep_time)
    else:
        print("Preparation time must be a positive integer.")
        return
    if not name or not ingredients or not meal or not prep_time:
        print("Recipes data cannot be empty.")
        return

    cookbook[name] = {
        "ingredients": [ingredient.strip() for ingredient in ingredients],
        "meal": meal,
        "prep_time": prep_time
    }
    print(f"Recipe '{name}' has been added to the cookbook.")

# Part 2: Command Line Interface

print("Welcome to the Python Cookbook!")

while True:
    print ("------------------")
    print ("------------------")
    print("List of available options:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")

    choice = input("Please select an option: ")

    if choice == "1":
        add_recipe()
    elif choice == "2":
        recipe_name = input("Please enter a recipe name to delete: ")
        delete_recipe(recipe_name)
    elif choice == "3":
        recipe_name = input("Please enter a recipe name to get its details: ")
        print_recipe_details(recipe_name)
    elif choice == "4":
        print_recipe_names()
    elif choice == "5":
        print("Cookbook closed. Goodbye!")
        break
    else:
        print("Sorry, this option does not exist.")
