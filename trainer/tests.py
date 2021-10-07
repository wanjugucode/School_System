from django.conf.urls import url
from django.test import TestCase
from trainer.models import Trainer
from django.urls import reverse

# Create your tests here.
class TrainerModelTestCase(TestCase):
    def setUp(self):
        self.trainer=Trainer(
            first_name="John",
            last_name="Owour",
            course="Kotlin",
            gender="Male"
        )
    def test_trainer_name_contains_first_name(self):
        self.assertIn(self.trainer.first_name,self.trainer.full_name())
    
    def test_fullname_contains_last_name(self):
         self.assertIn(self.trainer.last_name,self.trainer.full_name())
    
    def test_register_trainer_view(self):
        url=reverse('register_trainer')
        data={
        "first_name":self.trainer.first_name,
        "last_name":self.trainer.last_name
    }
        request=self.client.post(url,data)
        self.assertEqual(request.status_code,200)

       