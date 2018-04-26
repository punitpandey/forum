from django import forms
class queryForm(forms.Form):
    name=forms.CharField(max_length="50")
    subject=forms.CharField(max_length="150")
    query=forms.CharField(max_length="1000")
    image=forms.FileField()

class responseForm(forms.Form):
    response=forms.CharField(max_length="500")