"""Define type for folder entity"""
import graphene
from graphene_django import DjangoObjectType

from folder.models import Folder


class FolderType(DjangoObjectType):
    """Define type for folder entity"""
    class Meta:
        """Set model which used for this type"""
        model = Folder
        fields = ('id', 'name', 'previous')
