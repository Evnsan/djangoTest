from django import forms
from .models import Picture, Observation

class UploadPictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['title', 'picture_file']

class ObservationForm(forms.ModelForm):
    class Meta:
        model = Observation
        fields = ['build', 'description']
