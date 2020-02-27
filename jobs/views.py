from django.shortcuts import render, get_object_or_404
from .models import Job

# Create your views here.
def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs': jobs})

#add job_id since we need an int variable

def detail(request, job_id):
    #pk->primary key in the database

    job_detail= get_object_or_404(Job, pk=job_id)

    return render(request, 'jobs/detail.html', {'job':job_detail})
