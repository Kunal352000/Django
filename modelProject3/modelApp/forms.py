from django import forms 
from .models import Student
class StudentForm(forms.ModelForm):
    #fields with validation
    class Meta:
        model=Student
        fields='__all__'