from django import forms
from django.utils.translation import gettext_lazy as _

class ImageUploadForm(forms.Form):
    avatar = forms.ImageField(label=_('Avatar'), required=False)
    cover = forms.ImageField(label=_('Cover'), required=False)

class ContactForm(forms.Form):
    name = forms.CharField(label=_('Name'), max_length=100)
    phone = forms.IntegerField(label=_('Contact Number'), required=False)
    email = forms.EmailField(label=_('Email'), max_length=100)
    message = forms.CharField(label=_('Message'), widget=forms.Textarea)