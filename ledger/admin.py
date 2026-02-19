from django.contrib import admin

from .models import Recipe, RecipeIngredient

# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe


class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)