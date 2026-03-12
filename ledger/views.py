from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

from .models import Recipe, Ingredient, RecipeImage
from .forms import RecipeForm, RecipeImageForm

# Create your views here.


def index(request):
    return HttpResponse("Welcome to Gabe's Recipe Book")


def recipes_list(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, "ledger/recipes_list.html", context)


@login_required
def recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    recipe_name = recipe.name
    recipe_ingredients = Ingredient.objects.filter(
                        recipe__recipe__name=recipe_name)
    context = {
        'recipe': recipe,
        'ingredients': recipe_ingredients
    }

    return render(request, "ledger/recipe_detail.html", context)


class RecipeImageAddView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    form_class = RecipeImageForm
    template_name = "ledger/recipe_add_image.html"

    def get_success_url(self):
        return reverse_lazy('ledger:recipe_detail',
                            kwargs={'pk': self.object.recipe.pk})


class RecipeAddView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm

    def get_success_url(self):
        return reverse_lazy('ledger:recipe_detail',
                            kwargs={'pk': self.object.pk})
