from django.shortcuts import render
from .models import (Job , JobCategory , JobType)
# Create your views here.

def job_listing(request):
    jobs = Job.objects.all()
    

    if request.method == 'POST':
        #print(request.POST)
        if request.POST['category'] != 'all':
            jobs = jobs.filter(category = request.POST['category'])
        if 'typecb' in request.POST.keys():
            # job_types = []
            # for x in request.POST['typecb']:
            #     job_types.append(JobType.objects.get(x))
            jobs = jobs.filter(type__in = request.POST['typecb'])

    
    job_count = len(jobs)
    context = {
        'jobs':jobs,
        'job_count': job_count,
        'categories' : JobCategory.objects.all(),
        'types' : JobType.objects.all()
        }
    return render(request,'jobportal/job_listing.html' , context)

