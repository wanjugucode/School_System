from django import urls
from django.urls import path
from .views import edit_course, register_course,course_list


urlpatterns = [
    path('register',register_course,name='register_course'),
    path('list/',course_list,name='course_list'), # str:code if it is a string
    path('edit/<int:id>/',edit_course,name='edit_course')
]
