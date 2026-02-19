from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe

# Create your views here.


def index(request):
    return HttpResponse("Welcome to Gabe's Recipe Book")


def recipes_list(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, "ledger/recipes_list.html", context)


def recipe(request, recipe_idx):
    

    recipe_context = context["recipes"][recipe_idx - 1]
    return render(request, "ledger/ingredients_list.html", recipe_context)
