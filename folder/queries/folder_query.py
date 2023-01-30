"""Query for accessing data from folder table/model."""
import graphene
from django.db.models.query import QuerySet

from folder.models import Folder
from folder.types import FolderType


class FolderQuery(graphene.ObjectType):
    """Query for accessing data from folder table/model."""
    folders = graphene.List(FolderType, id=graphene.ID())
    folder_by_name = graphene.Field(FolderType, name=graphene.String(required=True))

    @staticmethod
    def resolve_folders(root, info, id: int=None) -> QuerySet[Folder]:
        """Get all folders inside another folder."""
        if not id:
            return Folder.object.filter(name='root')

        return Folder.objects.filter(pk=id)

    @staticmethod
    def resolve_folder_by_name(root, info, name: str) -> QuerySet[Folder]:
        """Find folder by name."""

        return Folder.objects.filter(name=name)
