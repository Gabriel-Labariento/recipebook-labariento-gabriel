from django.urls import path

from .views import recipes_list, recipe

urlpatterns = [
    path('recipes/list/', recipes_list, name='recipes_list'),
    path('recipe/<int:recipe_number>/', recipe, name='recipe')
]

app_name = "ledger"
