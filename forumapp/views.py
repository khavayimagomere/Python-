from django.shortcuts import render
from django.shortcuts import HttpResponse 
from .models import Student, Empathy
from rest_framework import viewsets
from .serializers import StudentSerializer


# Create your views here.
def welcome(request):
    return render(request, 'forumapp.html')
    
def students(request):
    students = Student.objects.all()
    
    context = {
        'students':students
    }
    return render(request, 'forumapp.html', context)
    

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

