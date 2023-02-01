"""Schema."""
import graphene
from common.queries import GeneralQuery

schema = graphene.Schema(query=GeneralQuery)
