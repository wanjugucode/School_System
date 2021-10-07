from django.conf.urls import url
from django.db.models.query_utils import select_related_descend
from django.test import TestCase
from django.utils import safestring

import event
from event.models import Event
from django.urls import reverse

# Create your tests here.
class EventModelTestCase(TestCase):
    def setUp(self):
        self.event=Event(
            title="Ask a techie"
        )
    def test_register_event_view(self):
        url=reverse('event:calendar')
        data={
            "title":self.event.title
        }
        request=self.client.post(url,data)
        self.assertEqual(request.status_code,200)