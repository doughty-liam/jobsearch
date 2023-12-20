import graphene
from graphene_django import DjangoObjectType
from jobs import models

class JobType(DjangoObjectType):
    class Meta:
        model = models.Job

class Query(graphene.ObjectType):
    
    job = graphene.Field(JobType)

    def resolve_job(root, info):
        return (
            models.Job.objects.first()
        )
    
schema = graphene.Schema(query=Query)