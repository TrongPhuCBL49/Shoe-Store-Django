from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from .models import CustomerUser
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import NON_FIELD_ERRORS

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username',
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'Username'",
            }
        ),
        error_messages={'required': 'Username is required!'}
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'Password'",
            }
        ),
        error_messages={'required': 'Password is required!'}
    )


class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username',
            }
        ),
        error_messages={'required': 'Username is required!'}
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email Address',
            }
        ),
        error_messages={'required': 'Email Address is required!'}
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
            }
        ),
        error_messages={'required': 'Password is required!'}
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirm Password',
            }
        ),
        error_messages={'required': 'Confirm Password is required!'}
    )
    first_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'First name',
        }
    ))
    last_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Last name',
        }
    ))
    country = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Country',
        }
    ))
    phone_number = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Phone number',
        }
    ))
    province = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Province',
        }
    ))
    distric = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Distric',
        }
    ))
    address = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Address',
        }
    ))
    postcode = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Postcode/ZIP',
        }
    ))

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken!")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email is taken!")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Password must match!")
        return data
