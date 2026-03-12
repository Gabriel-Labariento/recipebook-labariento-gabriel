from django.urls import path

from .views import recipes_list, recipe, RecipeAddView, RecipeImageAddView

urlpatterns = [
    path('recipes/list/', recipes_list, name='recipes_list'),
    path('recipe/<int:recipe_number>/', recipe, name='recipe'),
    path('recipe/add/', RecipeAddView.as_view(), name='recipe_add'),
    path('recipe/<int:pk>/add_image', RecipeImageAddView.as_view(), name='add_recipe_image')
]

app_name = "ledger"
