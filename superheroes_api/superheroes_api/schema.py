"""Superheroes project schema"""

import graphene

from superheroes.schema import (
    Query as SuperheroesQuery,
    Mutation as SuperheroesMutation
)


class Query(SuperheroesQuery, graphene.ObjectType):
    """Schema Query object"""
    pass


class Mutation(SuperheroesMutation, graphene.ObjectType):
    """Schema Mutation object"""
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
