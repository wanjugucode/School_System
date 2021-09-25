from django import forms
from django.db.models.base import Model
from django.forms import fields
from.models import Event

class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model=Event
        fields="__all__"
        