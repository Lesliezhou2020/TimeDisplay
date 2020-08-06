from django.shortcuts import render, HttpResponse
from time import gmtime, strftime

# Create your views here.

def index(request):
    #return HttpResponse(strftime("%Y-%m-%d %H-%M %p", gmtime()))

    dt = strftime("%Y-%m-%d %H:%M %p", gmtime())

    context = {
        'time': dt
    }
    return render(request, 'index.html', context)
