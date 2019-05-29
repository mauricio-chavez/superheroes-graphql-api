"""Superheroes admin site"""

from django.contrib import admin

from .models import Superhero, Villain


admin.site.register(Superhero)
admin.site.register(Villain)
