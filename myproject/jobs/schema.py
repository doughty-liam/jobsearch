import graphene
from graphene_django import DjangoObjectType
from jobs.models import Job

class JobType(DjangoObjectType):
    class Meta:
        model = Job
        fields = ("id", "title", "company_name", "location", "description", "dateAdded", "applied")

class Query(graphene.ObjectType):
    
    all_jobs = graphene.List(JobType)

    def resolve_all_jobs(root, info):
        return Job.objects.all()
    
schema = graphene.Schema(query=Query)