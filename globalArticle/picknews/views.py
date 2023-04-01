from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'base.html')

def popup(request):
    return render(request, 'keyword_alert,html')

@login_required(login_url='/common/login')
def subs(request):
    return render(request, 'picknews/subscription.html')
    #return HttpResponse("Hi")