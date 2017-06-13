from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
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
        fields = ['first_name', 'last_name', ]


class ProfileForm(forms.ModelForm):
    # nickname = forms.CharField(max_length=255)
    profile_photo = forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ['nickname', 'profile_photo']

'''       
class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    nickname = forms.CharField(max_length=255)
'''