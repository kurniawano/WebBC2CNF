from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context={}
    return render(request, 'bc2cnf/index.html', context)

def submit(request):
    return HttpResponse('Submitted.')
