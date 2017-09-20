from .models import Student, Empathy
from rest_framework import serializers
class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'course', 'year', 'email')
        
      #  model = Empathy
       # fields = ('title', 'location', 'trainer')
