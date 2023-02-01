"""Queries form all apps."""
import graphene
from files.queries import FilesQuery
from folder.queries import FolderQuery


class GeneralQuery(FilesQuery, FolderQuery, graphene.ObjectType):
    """Queries form all apps."""
    pass
