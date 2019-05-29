"""Superheroes app models"""

from django.db import models


class Superhero(models.Model):
    """Superhero model"""
    name = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    alter_ego = models.CharField(max_length=50)
    first_appearance = models.CharField(max_length=50)
    characters = models.CharField(max_length=100)
    enemy = models.ForeignKey('Villain', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """Returns a string representation of superhero"""
        return self.name
    
    class Meta:
        verbose_name_plural = 'Superheroes'


class Villain(models.Model):
    """Villain model"""
    name = models.CharField(max_length=50)
    alter_ego = models.CharField(max_length=50)

    def __str__(self):
        """Returns a string representation of villain"""
        return self.name
