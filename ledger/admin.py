from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Profile, Recipe, RecipeIngredient, RecipeImage

# Register your models here.


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,]


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeImageInline(admin.StackedInline):
    model = RecipeImage


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline, RecipeImageInline]

    fieldsets = [
        ('Details', {
            'fields': [
                ('name', 'author'),
            ]
        })
    ]


admin.site.register(Recipe, RecipeAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
