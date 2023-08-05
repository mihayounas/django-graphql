import graphene
from graphene_django.types import DjangoObjectType
from .models import Item

class ItemType(DjangoObjectType):
    class Meta:
        model = Item

class Query(graphene.ObjectType):
    all_items = graphene.List(ItemType)

    def resolve_all_items(self, info):
        return Item.objects.all()

class CreateItem(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    item = graphene.Field(ItemType)

    def mutate(self, info, name):
        item = Item(name=name)
        item.save()
        return CreateItem(item=item)

class Mutation(graphene.ObjectType):
    create_item = CreateItem.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
