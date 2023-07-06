from typing import Any, Dict
from django import forms
from django.core import validators
class FeedBackForm(forms.Form):
    name=forms.CharField()
    rollno=forms.CharField()
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea)

    def clean_name(self):
        print("this is my cleaned_data",self.cleaned_data)
        inputName=self.cleaned_data['name']
        print("this is input name",inputName)
        if len(inputName) < 4:
            # print("yes i am here")
            raise forms.ValidationError('trial stop must be >= movement start')
        return inputName

    def clean_rollno(self):
        inputRoll=self.cleaned_data['rollno']
        if len(inputRoll)>0:
            print(len(inputRoll))
            raise forms.ValidationError("Roll number is noty zero")