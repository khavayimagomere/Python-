from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog, Reader 


# Create your views here.
def list(request):
    return render(request, 'forumapp.html')
    
def details(request):
    return HttpResponse("Thank you Vallary i appreciate your effort.")
    
def update(request):
    return HttpResponse('Learn to create opportunities to synergizeand be with other people efficiently.')
    