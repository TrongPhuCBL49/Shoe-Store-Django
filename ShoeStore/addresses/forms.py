from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import NON_FIELD_ERRORS

class AddressForm(forms.Form):
    country = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Country',
        }
    ))
    province = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Province',
        }
    ))
    district = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'District',
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
