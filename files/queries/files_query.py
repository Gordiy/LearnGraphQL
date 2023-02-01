"""Query for accessing data from File table/model."""
import graphene

from files.models import Files
from files.types import FilesType
from graphene_django.filter import ListFilter


class FilesQuery(graphene.ObjectType):
    """Query for accessing data from File table/model."""
    files = graphene.Field(FilesType)
    file_by_name = graphene.Field(FilesType, name=graphene.String(required=True))

    @staticmethod
    def resolver_files_by_name(root, info, name: str) -> Files or None:
        """Get file by name."""
        try:
            return Files.objects.get(name=name)
        except Files.DoesNotExist:
            return None

