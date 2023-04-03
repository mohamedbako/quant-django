from django.shortcuts import render
from .models import Job
# Create your views here.


def jobList(request):
    jobList = Job.objects.all()
    context = {'jobs' : jobList}
    return render(request, 'job/jobs.html', context)

def jobDetail(request, id):
    jobDetail = Job.objects.get(id = id)
    context = {'job' : jobDetail}
    return render(request, 'job/jobDetail.html', context)

def jobApply(request):
    jobList = Job.objects.all()
    context = {'jobs' : jobApply}
    return render(request, 'job/jobApply.html', context)
