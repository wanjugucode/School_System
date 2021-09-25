
from django.db import models
from django.db.models import fields
from django.db.models.base import Model

from rest_framework import serializers

from student.models import Student
from trainer.models import Trainer
from course.models import Course
from event.models import Event

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student                                                                                                                                           
        fields=("first_name","last_name","age","gender")

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trainer
        fields=("first_name","last_name","gender","course")

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=("course_code","course_name")

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields=("title","description")



