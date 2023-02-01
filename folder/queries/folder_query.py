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
    def resolve_folders(root, info, id: int or None) -> QuerySet[Folder]:
        """Get all folders inside another folder."""
        if not id:
            root_folder = Folder.objects.get(name='root')
            return Folder.objects.filter(previous=root_folder)

        return Folder.objects.filter(pk=id)

    @staticmethod
    def resolve_folder_by_name(root, info, name: str) -> Folder or None:
        """Get folder by name."""

        try:
            return Folder.objects.get(name=name)
        except Folder.DoesNotExist:
            return None
