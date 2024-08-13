from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField(label='ایمیل خود را وارد کنید', required=True)