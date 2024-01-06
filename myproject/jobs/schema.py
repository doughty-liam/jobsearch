import graphene
from graphene_django import DjangoObjectType
from jobs.models import Job

class JobType(DjangoObjectType):
    class Meta:
        model = Job

class Query(graphene.ObjectType):

    all_jobs = graphene.List(JobType)
    jobs_by_date_added = graphene.List(JobType, keyword=graphene.String(required=True))

    def resolve_all_jobs(root, info, keyword):
        return Job.objects.all()
    
    def resolve_jobs_by_date_added(root, info, keyword):
        return Job.objects.order_by('-dateAdded').filter(description__contains=keyword) # minus sign used to sort in descending order