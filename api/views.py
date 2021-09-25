from event.models import Event
from course.models import Course
from trainer.models import Trainer
from student.models import Student
from django.shortcuts import render
from rest_framework.serializers import Serializer

# Create your views here.
from. serializer import CourseSerializer, StudentSerializer, TrainerSerializer,EventSerializer
from rest_framework import viewsets


class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class TrainerViewSet(viewsets.ModelViewSet):
    queryset=Trainer.objects.all()
    serializer_class=TrainerSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset=Event.objects.all()
    serializer_class=EventSerializer
