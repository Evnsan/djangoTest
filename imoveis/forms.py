from django import forms
from .models import Picture, Observation, Owner, PhoneNumber

class UploadPictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['title', 'picture_file']

class ObservationForm(forms.ModelForm):
    class Meta:
        model = Observation
        fields = ['build', 'description']

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['name', 'email']

class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = PhoneNumber
        fields = ['owner', 'country', 'state', 'number']
