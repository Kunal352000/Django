from django.shortcuts import render
from jobsInfo.models import *
# Create your views here.

def homepage_view(request):
    return render(request,'jobsInfo/index.html')

def hydJobs_view(request):
    hyd_jobs = hydJobs.objects.all()
    # print(hyd_jobs)
    my_dict = {'hyd_jobs': hyd_jobs}
    print("hey")
    return render(request,'jobsInfo/hydJobs.html',context=my_dict)

def bengalurujobs_view(request):
    jobs_list = BengaluruJobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'jobsInfo/bangJobs.html',context=my_dict)


def punejobs_view(request):
    jobs_list = BengaluruJobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'jobsInfo/puneJobs.html',context=my_dict)