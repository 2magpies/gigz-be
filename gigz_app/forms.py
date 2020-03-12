from django import forms
from .models import Venue, Audition

class VenueForm(forms.ModelForm):

    class Meta:
        model = Venue
        fields = ('name', 'website_url', 'auditions',)


class AuditionForm(forms.ModelForm):

    class Meta:
        model = Audition
        fields = ('title', 'description', 'roles','date', 'time', 'location', 'venue',)

        