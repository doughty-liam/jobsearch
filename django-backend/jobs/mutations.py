import graphene
from graphene_django import DjangoObjectType
from jobs.models import Job

class JobType(DjangoObjectType):
    class Meta:
        model = Job

class applied(graphene.Mutation):

    id = graphene.Int()
    title = graphene.String()
    applied = graphene.String()

    class Arguments:
        jobid = graphene.Int()

    def mutate(cls, info, jobid):
        job = Job.objects.get(id=jobid)
        job.applied = True
        job.save()

        return applied(id=job.id, title=job.title, applied=job.applied)
    
class Mutation(graphene.ObjectType):
    applyToJob = applied.Field()
