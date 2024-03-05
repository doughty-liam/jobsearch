import graphene
from graphene_django import DjangoObjectType
from jobs.models import Job

class JobType(DjangoObjectType):
    class Meta:
        model = Job

class Query(graphene.ObjectType):

    all_jobs = graphene.List(JobType)
    jobs_by_date_added = graphene.List(JobType, keyword=graphene.String(required=True))
    jobs_by_similarity = graphene.List(JobType)

    def resolve_all_jobs(root, info, keyword):
        return Job.objects.all()
    
    def resolve_jobs_by_date_added(root, info, keyword):
        return Job.objects.order_by('-date_added').filter(description__contains=keyword) # minus sign used to sort in descending order
    
    def resolve_jobs_by_similarity(root, info):
        return Job.objects.order_by('-similarity_rating')
