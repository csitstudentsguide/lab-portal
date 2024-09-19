from django.shortcuts import render
# Create your views here.

def expLists_home(request):
    return render(request, 'expLists/expLists_home.html')
