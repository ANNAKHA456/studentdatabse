from django import forms

class StudForm(forms.Form):
    s_name=forms.CharField(max_length=30,label='STUDENT NAME')
    s_class=forms.CharField(max_length=30,label='Class')
    s_address=forms.CharField(max_length=30,label='ADDRESS')
    s_school=forms.CharField(max_length=30,label='School name')
    s_email=forms.EmailField(max_length=30,label='School email')

class SForm(forms.Form):
    s_name=forms.CharField(max_length=30)