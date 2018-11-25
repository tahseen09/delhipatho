from django import forms

class Form(forms.Form):
    id = forms.CharField(label="Report ID", max_length=100)
    