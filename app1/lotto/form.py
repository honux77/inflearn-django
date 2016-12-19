from django import forms
from .models import GuessNumbers

class PostForm(forms.ModelForm):

    class Meta:
        model = GuessNumbers
        fields = ('name', 'text', 'numbers',)
