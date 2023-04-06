from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Job
from .form import ApplyForm

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

    if request.method =='POST':
        form = ApplyForm(request.POST, request.FILES)
    if form.is_valid():
            myForm = form.save(commit=False)
            myForm.job = jobApply
            myForm.save()
    else:
        form = ApplyForm()



    context = {'job' : jobApply, 'form' : form}
    return render(request, 'job/jobApply.html', context)

 