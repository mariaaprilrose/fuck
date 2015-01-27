from django import forms
from django.utils.translation import gettext_lazy as _

class BlogForm(forms.Form):
	title = forms.CharField(label=_('Title'), max_length=100)
	picture = forms.ImageField(label=_('Picture'), required=False)
	content = forms.CharField(widget=forms.Textarea)