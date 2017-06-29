from django.contrib.auth.models import User
from django import forms

from .models import Photo, Profile

class UploadForm(forms.ModelForm):
    comment = forms.CharField(max_length=255)
    class Meta:
        model = Photo
        exclude = ('thumnail_image', 'owner')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name',]

class ProfileForm(forms.ModelForm):
    profile_photo = forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ['nickname', 'profile_photo']
