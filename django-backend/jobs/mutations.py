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

    def mutate(root, info, jobid):
        job = Job.objects.get(id=jobid)
        job.applied = not job.applied
        job.save()

        return job_applied(id=job.id, title=job.title, applied=job.applied)

    
class job_shortlist(graphene.Mutation):
    
    id = graphene.Int()
    title = graphene.String()
    shortlisted = graphene.Boolean()

    class Arguments:
        jobid = graphene.Int()

    def mutate(root, info, jobid):
        job = Job.objects.get(id=jobid)
        job.shortlisted = not job.shortlisted
        job.save()

        return job_shortlist(id=job.id, title=job.title, shortlisted=job.shortlisted)

    
class Mutation(graphene.ObjectType):
    applyToJob = job_applied.Field()
    shortlistJob = job_shortlist.Field()