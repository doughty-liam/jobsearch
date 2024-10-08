import graphene
from graphene_django import DjangoObjectType
from jobs.models import Job

class JobType(DjangoObjectType):
    class Meta:
        model = Job

class Query(graphene.ObjectType):

    all_jobs = graphene.List(JobType, first=graphene.Int(required=True), skip=graphene.Int(required=True))
    jobs_by_date_added = graphene.List(JobType, first=graphene.Int(), skip=graphene.Int(), keyword=graphene.String(required=True))
    jobs_by_similarity = graphene.List(JobType, first=graphene.Int(), skip=graphene.Int(), isApplied=graphene.Boolean())

    def resolve_all_jobs(root, info, first, skip):
        qs = Job.objects.all()
        if skip:
            qs = qs[skip:]
        if first:
            qs = qs[:first]
        return qs    
    
    def resolve_jobs_by_date_added(root, info, first, skip, keyword):
        qs = Job.objects.order_by('-date_added').filter(description__contains=keyword)
        if skip:
            qs = qs[skip:]
        if first:
            qs = qs[:first]
        return qs
    
    def resolve_jobs_by_similarity(root, info, first, skip, isApplied):
        qs = Job.objects.order_by('-similarity_rating').filter(applied=isApplied)
        if skip:
            qs = qs[skip:]
        if first:
            qs = qs[:first]
        return qs
