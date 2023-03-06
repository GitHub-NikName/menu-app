from django import forms
from menu.models import Menu


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['title', 'parent', 'position', 'url', 'named_url']

    def clean_explicit_url(self):
        return self.cleaned_data['url'] or None

    def clean_named_url(self):
        return self.cleaned_data['named_url'] or None
