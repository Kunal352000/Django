from typing import Any, Dict
from django import forms
from django.core import validators
class FeedBackForm(forms.Form):
    name=forms.CharField()
    rollno=forms.CharField()
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40)])

    