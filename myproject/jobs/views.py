from django.shortcuts import render
from django.http import HttpResponse, Http404

def index(request):
    return render(request, 'jobs/index.html')

    ''' To throw an http error, use a try-except-raise block '''