from django.shortcuts import render
from .models import Job
# Create your views here.


def jobList(request):
    jobList = Job.objects.all()
    context = {'jobs' : jobList}
    return render(request, 'job/jobs.html', context)

def jobDetail(request, slug):
    jobDetail = Job.objects.get(slug = slug)
    context = {'job' : jobDetail}
    return render(request, 'job/jobDetail.html', context)

def jobApply(request, slug):
    jobApply = Job.objects.get(slug = slug)
    context = {'job' : jobApply}
    return render(request, 'job/jobApply.html', context)
