import graphene
import jobs.schema
import jobs.mutations

class Query(jobs.schema.Query, graphene.ObjectType):
    
    pass

class Mutation(jobs.mutations.Mutation, graphene.ObjectType):

    pass

schema = graphene.Schema(query=Query, mutation=Mutation)