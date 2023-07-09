from django import forms
from modelApp.models import student

class studentForm(forms.ModelForm):
    class Meta:
        model=student
        fields='__all__'