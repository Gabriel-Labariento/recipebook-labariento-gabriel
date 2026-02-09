from django.urls import path

from .views import index, recipes_list, recipe

urlpatterns = [
    path('', index, name='index'),
    path('recipes/list/', recipes_list, name='recipes_list'),
    path('recipe/<int:recipe_idx>/', recipe, name='recipe')
]

app_name = "ledger"
