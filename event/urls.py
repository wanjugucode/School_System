from django.urls import re_path as url
from django.urls import path
from . import views
app_name = 'event'
urlpatterns=[
 path('calendar/',views.CalendarView.as_view(), name='calendar'),
 path('register/', views.event, name='event_list'),
]