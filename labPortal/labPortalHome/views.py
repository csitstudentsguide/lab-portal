from django.shortcuts import render

# Create your views here.
def lab_portal_home(request):
    return render(request, 'labPortalHome/lab_portal_home.html')    
