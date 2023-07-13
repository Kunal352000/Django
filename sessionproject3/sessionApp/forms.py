from django import forms 
class AddItemForm(forms.Form):
    itemName=forms.CharField(max_length=50)
    quantity=forms.IntegerField()