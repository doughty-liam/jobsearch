import graphene
from graphene_django import DjangoObjectType
from jobs.models import Job

class JobType(DjangoObjectType):
    class Meta:
        model = Job

class job_applied(graphene.Mutation):

    id = graphene.Int()
    title = graphene.String()
    applied = graphene.String()

    class Arguments:
        jobid = graphene.Int()

    def mutate(cls, info, jobid):
        job = Job.objects.get(id=jobid)
        job.applied = True
        job.save()

        return job_applied(id=job.id, title=job.title, applied=job.applied)

    
class job_shortlist(graphene.Mutation):
    
    id = graphene.Int()
    title = graphene.String()
    shortlist = graphene.Boolean()

    class Arguments:
        jobid = graphene.Int()
        shortlist = graphene.Boolean()

    def mutate(cls, info, jobid, shortlist):
        job = Job.objects.get(id=jobid)
        job.shortlisted = shortlist
        job.save()

        return job_shortlist(id=job.id, title=job.title, shortlist=job.shortlisted)

    
class Mutation(graphene.ObjectType):
    applyToJob = job_applied.Field()
    shortlistJob = job_shortlist.Field()