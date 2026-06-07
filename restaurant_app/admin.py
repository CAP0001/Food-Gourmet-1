from django.contrib import admin
from .models import Food, Feedback
from modeltranslation.admin import TranslationAdmin

# Register your models here.
admin.site.register(Feedback)
@admin.register(Food)
class FoodAdmin(TranslationAdmin):
    list_display = ('name', 'description')