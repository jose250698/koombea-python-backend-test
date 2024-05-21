from django import forms
from .models import Page


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['url']
        widgets = {
            'url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter URL to scrape'}),
        }
