from typing import Any
from django import forms


class StudentRewgestion(forms.Form):
    first_name=forms.CharField()
    last_name=forms.CharField()
    email=forms.EmailField()
    batch=forms.IntegerField()
    password=forms.CharField(widget=forms.PasswordInput())
    repassword=forms.CharField(widget=forms.PasswordInput())
    textarea=forms.CharField(widget=forms.Textarea)


    def clean(self):
        clean_field=super().clean()
        password_match=self.cleaned_data['password']
        repassword_match=self.changed_data['repassword']
        if password_match !=repassword_match:
            raise forms.ValidationError('password not match')
        
        



