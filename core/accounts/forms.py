from django import forms
from .models import *

class EmailForm(forms.Form):
    email = forms.EmailField(label='ایمیل', widget=forms.EmailInput(attrs={'placeholder': 'ایمیل خود را وارد کنید'}))

class VerificationForm(forms.Form):
    code = forms.CharField(label='کد تایید', max_length=6, widget=forms.TextInput(attrs={'placeholder': 'کد 123456 را وارد کنید'}))

class CodeForm(forms.Form):
    code = forms.CharField(label='Verification Code', max_length=6)


class PasswordForm(forms.Form):
    password1 = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور'})
    )
    password2 = forms.CharField(
        label='تکرار رمز عبور',
        widget=forms.PasswordInput(attrs={'placeholder': 'تکرار رمز عبور'})
    )

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error('password2', 'رمزهای عبور مطابقت ندارند!')



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'image']
