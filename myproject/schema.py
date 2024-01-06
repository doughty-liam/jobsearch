import graphene
import jobs.schema

class Query(jobs.schema.Query, graphene.ObjectType):
    
    pass

schema = graphene.Schema(query=Query)