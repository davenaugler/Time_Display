from django.shortcuts import render
from time import gmtime, strftime
from datetime import datetime, time, timezone


# Create your views here.
def index(request):
    context = {
        # "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
        # "time": strftime("%m-%d-%Y %H:%M %p", gmtime())
        "time": strftime("%A, %B %d, %Y %H:%M %p", gmtime())
    }
    return render(request,'dtd_app/index.html', context) 