from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('recipes/list/', recipes_list, name='recipes_list'),
    path('recipe/<int:recipe_id>/', recipe, name='recipe' )
]

app_name = "ledger"