from django.urls import path

from .views import recipes_list, recipe, RecipeAddView

urlpatterns = [
    path('recipes/list/', recipes_list, name='recipes_list'),
    path('recipe/<int:recipe_number>/', recipe, name='recipe'),
    path('recipe/add/', RecipeAddView.as_view(), name='recipe_add')
]

app_name = "ledger"
