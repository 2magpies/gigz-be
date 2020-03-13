from rest_framework import serializers
from .models import Venue, Audition

class AuditionSerializer(serializers.ModelSerializer):
    
    class Meta:
       model = Audition
       fields = '__all__'  

class VenueSerializer(serializers.ModelSerializer):
    auditions = AuditionSerializer(many=True, read_only=True)

    class Meta:
       model = Venue
       fields = ['id', 'name', 'website_url', 'auditions',]


