import graphene
from graphene_django import DjangoObjectType
from jobs.models import Job
from jobs.jobSearch import JobPuller
from django.db.models import Q

class JobType(DjangoObjectType):
    class Meta:
        model = Job

class FilterParamsType(graphene.InputObjectType):
    '''
    Defines the filter/sort parameter input for the 'jobs' query.
    '''

    shortlisted = graphene.Boolean()
    applied = graphene.Boolean()
    keyword_str = graphene.String()

class Query(graphene.ObjectType):

    '''
    IDIOT!!!

    The filtering should all be done in ONE query as a result of the parameters passed.
    Sort order, applied or unapplied, shortlisted etc should be passed as a VARIABLE
    
    '''

    all_jobs = graphene.List(JobType, first=graphene.Int(), skip=graphene.Int())
    jobs_by_date_added = graphene.List(JobType, first=graphene.Int(), skip=graphene.Int(), keywordSet=graphene.String())
    jobs_by_similarity = graphene.List(JobType, first=graphene.Int(), skip=graphene.Int(), isApplied=graphene.Boolean())
    clear_all_jobs = graphene.String()
    get_new_jobs = graphene.String()
    shortlisted_jobs = graphene.List(JobType, first=graphene.Int(), skip=graphene.Int(), keywordSet=graphene.String())
    jobs = graphene.List(JobType, first=graphene.Int(), skip=graphene.Int(), filterParams=FilterParamsType())

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
    
    def resolve_shortlisted_jobs(root, info, first, skip, keywordSet):
        
        keywords = keywordSet.split(",") # Separate keywords by comma delim
        keyword_qset = Q()
        for word in keywords:
            keyword_qset &= Q(description__contains=word)
        

        qs = Job.objects.order_by('-date_added').filter(keyword_qset, shortlisted=True)

        if skip:
            qs = qs[skip:]
        if first:
            qs = qs[:first]
        return qs


    def resolve_jobs(root, info, first, skip, filterParams):
        
        # Vars will be a dictionary containing the filter/sort parameters

        shortlisted_q = Q(shortlisted=filterParams.shortlisted)
        applied_q = Q(applied=filterParams.applied)

        
        # Processing provided search keywords
        keyword_strs = filterParams.keyword_str.split(",")
        keyword_qset = Q()
        for word in keyword_strs:
            keyword_qset &= Q(description__contains=word)

        filter_qset = shortlisted_q & applied_q & keyword_qset

        qs = Job.objects.order_by('-date_added').filter(filter_qset)

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
        