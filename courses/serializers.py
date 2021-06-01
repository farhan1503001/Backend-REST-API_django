from django.db.models import fields
from rest_framework import serializers
from .models import Course
class CourseSerialize(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=('id','course','language','platform','price')

