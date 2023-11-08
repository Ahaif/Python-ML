import sys


class Recipe:
    def __init__(self, name , cooking_lv, cooking_time, ingredients, description, recipe_type):
        self.name = name
        self.cooking_lv = cooking_lv
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

        self.validate()
    
    def validate(self):
        if not 1 <= self.cooking_lv <= 5:
            raise ValueError("cooking_lv must be between 1 and 5")
        if self.cooking_time < 0:
            raise ValueError("cooking_time must be positive")
        if self.recipe_type not in ["starter", "lunch", "dessert"]:
            raise ValueError("recipe_type must be starter, lunch or dessert")
        if not isinstance(self.ingredients, list):
            raise ValueError("ingredients must be a list")
        
        for ingredient in self.ingredients:
            if not isinstance(ingredient, str):
                raise ValueError("ingredients must be a list of strings")
    def __str__(self):
        txt = f""
        txt += f"recipe for {self.name}:\n"
        txt += f"cooking_lv: {self.cooking_lv}\n"
        txt += f"cooking_time: {self.cooking_time}\n"
        txt += f"ingredients: {self.ingredients}\n"
        txt += f"description: {self.description}\n"
        txt += f"recipe_type: {self.recipe_type}\n"
        return txt
    
    
    