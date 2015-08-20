from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from .models import Submission, SubmissionForm
from subprocess import call

# Create your views here.
#def index(request):
#    context={}
#    return render(request, 'bc2cnf/index.html', context)

def index(request):
    if request.method=='POST':
	form = SubmissionForm(request.POST, request.FILES)
	if form.is_valid():
	    form.save(form.userid)
	    return convert(request, form)
    else:
        form = SubmissionForm()
    return render(request, 'bc2cnf/index.html',{'form':form})	

def convert(request, form):
    filename=request.FILES['bcfile'].name    
    filenameNoExt=filename.split('.')[0]
    print filenameNoExt
    outname=filenameNoExt+'.cnf'
    fullpath='files/'+filenameNoExt
    call(['bc2cnf','-v','-nosimplify','-nocoi',fullpath+'.bc',fullpath+'.cnf'])
    return render_to_response('bc2cnf/convert.html',{'form':form})
