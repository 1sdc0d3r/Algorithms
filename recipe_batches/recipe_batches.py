#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    max = math.inf
    for ingName in recipe:
        if ingName not in ingredients:
            max = 0
        elif ingredients[ingName] / recipe[ingName] < max:
            max = ingredients[ingName] / recipe[ingName]
    return math.floor(max)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 20, 'butter': 30, 'flour': 50}
    ingredients = {'milk': 400, 'butter': 150, 'flour': 102}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
