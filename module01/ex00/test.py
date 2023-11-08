from recipe import Recipe
from book import Book
from datetime import datetime

# Create some Recipe objects
recipe1 = Recipe("Pasta", 2, 30, ["pasta", "tomato sauce", "cheese"], "Classic pasta dish", "lunch")
recipe2 = Recipe("Salad", 1, 10, ["lettuce", "tomato", "cucumber"], "Healthy salad", "starter")
recipe3 = Recipe("Brownie", 3, 45, ["flour", "eggs", "chocolate", "sugar"], "Delicious chocolate brownies", "dessert")

# Create a Book object
my_recipe_book = Book("My Recipe Book", datetime.now(), datetime.now(), [])

# Add the recipes to the book
my_recipe_book.add_recipe(recipe1)
my_recipe_book.add_recipe(recipe2)
my_recipe_book.add_recipe(recipe3)

# Test get_recipe_by_name
recipe_name = "Pasta"
found_recipe = my_recipe_book.get_recipe_by_name(recipe_name)
if found_recipe:
    print(f"Recipe found with name '{recipe_name}': {found_recipe}")
else:
    print(f"Recipe with name '{recipe_name}' not found")

# Test get_recipes_by_type
recipe_type = "starter"
recipes_by_type = my_recipe_book.get_recipes_by_type(recipe_type)
if recipes_by_type:
    print(f"{recipe_type.capitalize()} Recipes: {recipes_by_type}")
else:
    print(f"No {recipe_type} recipes found in the book")

# Add a recipe with the wrong type to test the error handling
invalid_recipe = Recipe("Invalid Recipe", 4, 25, ["ingredient1", "ingredient2"], "Invalid type", "invalid")
my_recipe_book.add_recipe(invalid_recipe)
