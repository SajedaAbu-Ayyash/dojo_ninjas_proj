from django.shortcuts import render, redirect
from . import models


# this function will return dojos and ninjas to jinja index.html
def index(request):
    context = {
        'dojos': models.display_dojos(),
        'ninjas' : models.display_ninjas()
    }
    return render(request, 'index.html', context)

def add_dojo(request):
    models.add_dojo(request)
    return redirect('/')

def add_ninja(request):
    models.add_ninja(request)
    return redirect('/')

def remove_dojo(request):
        if request.method == 'POST':
            models.remove_dojo(request.POST)
        return redirect('/')

# Create your views here.
