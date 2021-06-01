from django.db.models import fields
from rest_framework import serializers
from .models import Course
class CourseSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Course
        fields=('id','url','course','language','platform','price')

