from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe, Ingredient

# Create your views here.


def index(request):
    return HttpResponse("Welcome to Gabe's Recipe Book")


def recipes_list(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, "ledger/recipes_list.html", context)


def recipe(request, recipe_number):
    recipe_name = "Recipe {}".format(recipe_number)
    recipe = Recipe.objects.get(name=recipe_name)
    recipe_ingredients = Ingredient.objects.filter(recipe__recipe__name=recipe_name)
    context = {
        'recipe': recipe,
        'ingredients': recipe_ingredients
    }
    
    return render(request, "ledger/ingredients_list.html", context)
