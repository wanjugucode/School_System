# from django.urls import
from django.urls.conf import include, path
from rest_framework import routers, urlpatterns
from .views import StudentViewSet
from .views import TrainerViewSet
from .views import CourseViewSet
from .views import EventViewSet

router=routers.DefaultRouter()
router.register(r"students", StudentViewSet) # Raw string - alphanumeric expectation 
router.register(r"trainers",TrainerViewSet) 
router.register(r"courses",CourseViewSet)
router.register(r"events", EventViewSet)

urlpatterns=[
    path("",include(router.urls)),
]




