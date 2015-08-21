from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from .models import Submission, SubmissionForm
from subprocess import call
from StringIO import StringIO
from django.conf import settings
import os

# Create your views here.
#def index(request):
#    context={}
#    return render(request, 'bc2cnf/index.html', context)

def index(request):
    if request.method=='POST':
	uniqueid=request.POST['userid']
	split_name=request.FILES['bcfile'].name.split('.')
	new_name=split_name[0]+'_'+uniqueid+'.'+split_name[1]
	request.FILES['bcfile'].name=new_name
	form = SubmissionForm(request.POST, request.FILES)
	if form.is_valid():
	    form.save()
	    return convert(request, form)
    else:
        form = SubmissionForm()
    return render(request, 'bc2cnf/index.html',{'form':form})	

def convert(request, form):
    filename=request.FILES['bcfile'].name    
    filenameNoExt=filename.split('.')[0]
    outname=filenameNoExt+'.cnf'
    fullpath=settings.MEDIA_ROOT+filenameNoExt
    call(['bc2cnf','-v','-nosimplify','-nocoi',fullpath+'.bc',fullpath+'.cnf'])
    fdownld=StringIO(file(fullpath+'.cnf','r').read())
    call(['rm',fullpath+'.bc'])
    call(['rm',fullpath+'.cnf'])
    #return HttpResponse(fdownld.read(),content_type='text/plain')
    return render_to_response('bc2cnf/convert.html',{'fdownld':fdownld.read()})
