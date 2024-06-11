from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def labPortalHome(request):
    return HttpResponse('This is Lab Portal Home ...')
