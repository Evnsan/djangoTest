from django import forms

from ..models import Build, Observation
from ..widgets.widgets import BootstrapedCheckboxSelectMultiple

class ObservationAdminForm(forms.ModelForm):
    class Meta:
        model = Observation
        fields = ['description']
        widgets = {
            'description': forms.Textarea
        }


class BuildForm(forms.ModelForm):
    class Meta:
        model = Build
        exclude = []
        widgets = {
                'features': BootstrapedCheckboxSelectMultiple(),
                'owners': BootstrapedCheckboxSelectMultiple()
        }
