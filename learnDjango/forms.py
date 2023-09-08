from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name of the List", max_length=200, required=False)
    check = forms.BooleanField(required=False)