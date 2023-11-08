import sys

from recipe import Recipe

from datetime import datetime


class Book:
    def __init__(self, name, last_update, creation_date, recipes_list):
        self.name = name
        self.last_update = last_update
        self.creation_date = creation_date
        self.recipes_list = recipes_list

        self.validate()

    def validate(self):
        if not isinstance(self.name, str):
            raise ValueError("name must be a string")
        # if not isinstance(self.last_update, datetime):
        #     raise ValueError("last_update must be a datetime")
        # if not isinstance(self.creation_date, datetime):
        #     raise ValueError("creation_date must be a datetime")
        if not isinstance(self.recipes_list, list):
            raise ValueError("recipes_list must be a list")
    
    def get_recipe_by_name(self, name):
        for recipe in self.recipes_list:
            if recipe.name == name:
                # print(recipe)
                return recipe
        print(f"recipe {name} not found")

    def get_recipes_by_type(self, recipe_type):
        if recipe_type in self.recipes_list:
            return [recipe.name for recipe in self.recipes_list[recipe_type]]
        else:
            return []
    
    def add_recipe(self, recipe):
        if not isinstance(recipe, Recipe):
            raise ValueError("recipe must be a Recipe object")
        self.recipes_list.append(recipe)
        self.last_update = datetime.now()
        print(f"recipe {recipe.name} added to the book")



