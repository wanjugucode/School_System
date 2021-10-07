from django import urls
from django.test import TestCase
from course.models import Course
from django.urls import reverse,resolve

# Create your tests here.
class CourseModelTestCase(TestCase):
    def setUp(self):
        self.course=Course(
        course_name="Kotlin",
        )
    def test_register_course_view(self):
        url=reverse('register_course')
        data={
          "course_name":self.course.course_name,
        }
        request=self.client.post(url,data)
        self.assertEqual(request.status_code,200)

    
    