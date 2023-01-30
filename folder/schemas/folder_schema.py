"""Schema for accessing to Folder model."""
import graphene

from folder.queries import FolderQuery

schema = graphene.Schema(query=FolderQuery)
