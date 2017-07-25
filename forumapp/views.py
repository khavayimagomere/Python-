from django.shortcuts import render
from django.shortcuts import HttpResponse 
from .models import Student, Empathy

# Create your views here.
def lists(request):
    return render(request, 'forumapp.html')
def create(request):
    return HttpResponse('Lovely people are the kind ones.')
def details(request):
    return HttpResponse('Work hard and put in the work.God will bless you.')