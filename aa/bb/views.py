from django.shortcuts import render
from .models import *
# Create your views here.
def cv(request):
    vv = CV.objects.all()
    return render(request,'lo.html',{'ab':vv})
