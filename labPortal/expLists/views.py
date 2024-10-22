from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import ExpListUploadForm
from .models import ExpLists

# Create your views here.

def expLists_home(request):
    return render(request, 'expLists/expLists_home.html')

def upload_exp(request):    
    if request.method == 'POST':
        form = ExpListUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()            
            return HttpResponseRedirect(reverse('show-expl-lists'))
    else:
        form = ExpListUploadForm()    

    return render(request, 'expLists/upload_exp.html', {'form':form})
    
def show_exp_lists(request):    
    all_exp = ExpLists.objects.all().values()
    return render(request, 'expLists/show_exp.html', {'all_exp':all_exp})
