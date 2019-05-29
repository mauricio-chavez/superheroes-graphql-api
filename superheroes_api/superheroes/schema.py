"""Superheroes schema"""

import graphene
from graphene_django import types

from .models import Superhero, Villain


# Objects

class SuperheroType(types.DjangoObjectType):
    """
    Superhero Object Type

    type Superhero {
        name: String!
        publisher: String!
        alter_ego: String!
        first_appearance: String!
        characters: String!
        enemy: Villain!
    }

    """
    class Meta:
        model = Superhero


class VillainType(types.DjangoObjectType):
    """
    Villain Object Type

    type Villain {
        name: String!
        alter_ego: String!
    }

    """
    class Meta:
        model = Villain


class VillainInput(graphene.InputObjectType):
    """Villain input type"""
    villain_id = graphene.ID()
    name = graphene.String()


class SuperheroMutation(graphene.Mutation):
    """Superhero Mutation"""
    class Arguments:
        name = graphene.String(required=True)
        publisher = graphene.String(required=True)
        alter_ego = graphene.String(required=True)
        first_appearance = graphene.String(required=True)
        characters = graphene.String(required=True)
        enemy = VillainInput(required=True)

    superhero = graphene.Field(SuperheroType)

    def mutate(self, info, **kwargs):
        """Saves the superhero into database"""
        enemy = kwargs.pop('enemy')
        villain_id = enemy.get('villain_id')
        name = enemy.get('name')

        if villain_id:
            villain_id = int(villain_id)
            villain = Villain.objects.get(id=villain_id)

        if name:
            villain = Villain.objects.get(name=name)

        kwargs['enemy'] = villain

        superhero = Superhero.objects.create(**kwargs)
        return SuperheroMutation(superhero=superhero)


# Query and Mutation types

class Query:
    """Superheroes Query Object"""
    all_superheroes = graphene.List(
        SuperheroType,
        publisher=graphene.String()
    )
    all_villains = graphene.List(
        VillainType,
        publisher=graphene.String()
    )
    superhero = graphene.Field(
        SuperheroType,
        id=graphene.ID(),
        name=graphene.String()
    )
    villain = graphene.Field(
        VillainType,
        id=graphene.ID(),
        name=graphene.String()
    )

    # Resolvers
    def resolve_all_superheroes(self, info, **kwargs):
        """allSuperheroes resolver"""
        query = Superhero.objects.select_related('enemy').all()

        publisher = kwargs.get('publisher')

        if publisher:
            return query.filter(publisher=publisher)

        return query

    def resolve_all_villains(self, info, **kwargs):
        """allVillains resolver"""
        query = Villain.objects.all()

        publisher = kwargs.get('publisher')

        if publisher:
            return query.filter(publisher=publisher)

        return query

    def resolve_superhero(self, info, **kwargs):
        """superhero resolver"""
        superhero_id = kwargs.get('id')
        name = kwargs.get('name')

        if superhero_id:
            superhero_id = int(superhero_id)
            return Superhero.objects.get(id=superhero_id)

        if name:
            return Superhero.objects.get(name=name)

        return None

    def resolve_villain(self, info, **kwargs):
        """villain resolver"""
        villain_id = kwargs.get('id')
        name = kwargs.get('name')

        if villain_id:
            villain_id = int(villain_id)
            return Villain.objects.get(id=villain_id)

        if name:
            return Villain.objects.get(name=name)

        return None


class Mutation:
    """Superheroes Mutation Type"""
    create_superhero = SuperheroMutation.Field()
