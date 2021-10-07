from django.test import TestCase
from .models import Student
import datetime 
from django.urls import reverse


# Create your tests here.
class StudentModelTestCase(TestCase):
    def setUp(self) :
        self.student=Student(
        first_name="Anastsia",
        last_name="Karobia",
        language="English",
        age=20
         )

    def test_full_name_contains_first_name(self):
        self.assertIn(self.student.first_name,self.student.full_name()) # assersion
    
    def test_fullname_contains_last_name(self):
        self.assertIn(self.student.last_name,self.student.full_name())

    def test_student_year_of_birth(self):
        current_year=datetime.datetime.now().year
        year=current_year-self.student.age
        self.assertEqual(year,self.student.year_of_birth())

    def test_register_student_view(self):
        url=reverse('register_student')
        data={
        "first_name":self.student.first_name, 
        "last_name":self.student.last_name,
 
        }
        request=self.client.post(url,data)
        self.assertEqual(request.status_code,200)


    





