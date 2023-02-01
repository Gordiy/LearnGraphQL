"""Define type for folder entity."""
from graphene import relay
from graphene_django import DjangoObjectType

from files.models import Files


class FilesType(DjangoObjectType):
    """Define type for folder entity."""
    class Meta:
        """Set model which used for this type"""
        model = Files
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'folder__name': ['iexact']
        }
        fields = ('id', 'name', 'folder')
        interface = (relay.Node, )
