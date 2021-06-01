from django.shortcuts import render
from .serializers import CourseSerialize
from .models import Course
from rest_framework import viewsets
# Create your views here.
class course_view(viewsets.ModelViewSet):
    queryset=Course.objects.all() #Literally the database model
    serializer_class=CourseSerialize #The class which will serialize
