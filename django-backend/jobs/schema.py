import graphene
from graphene_django import DjangoObjectType
from jobs.models import Job
from jobs.jobSearch import JobPuller
from django.db.models import Q

class JobType(DjangoObjectType):
    class Meta:
        model = Job

class Query(graphene.ObjectType):

    all_jobs = graphene.List(JobType, first=graphene.Int(), skip=graphene.Int())
    jobs_by_date_added = graphene.List(JobType, first=graphene.Int(), skip=graphene.Int(), keywordSet=graphene.String())
    jobs_by_similarity = graphene.List(JobType, first=graphene.Int(), skip=graphene.Int(), isApplied=graphene.Boolean())
    clear_all_jobs = graphene.String()
    get_new_jobs = graphene.String()

    def resolve_all_jobs(root, info, first, skip):
        qs = Job.objects.all()
        if skip:
            qs = qs[skip:]
        if first:
            qs = qs[:first]
        return qs    
    
    def resolve_jobs_by_date_added(root, info, first, skip, keywordSet):

        keywords = keywordSet.split(",") # Separate keywords by comma delim
        keyword_qset = Q()
        for word in keywords:
            keyword_qset &= Q(description__contains=word)
        

        qs = Job.objects.order_by('-date_added').filter(keyword_qset)
        ''' NEED TO IMPLEMENT IN FRONT END
        1. Create input field for search terms
        2. Clean input field string to comma separated values, remove extra spaces, remove spaces between comma
        3. Pass string to graphql jobs_by_date_added_query'''

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

    def resolve_clear_all_jobs(root, info):
        Job.objects.all().delete()
        return "Cleared all jobs from the database."
    
    def resolve_get_new_jobs(root, info):
        puller = JobPuller()
        puller.getJobs()
        return "Database updated."
        