from django import forms

class UserForm(forms.Form):
    email = forms.EmailField(label='E-mail', max_length=100, required=True)
    password = forms.CharField(label='Password', max_length=100, required=True)