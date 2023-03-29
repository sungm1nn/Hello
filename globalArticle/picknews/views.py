from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'base.html')

def subs(request):
    return render(request, 'picknews/subscription.html')
    #return HttpResponse("Hi")