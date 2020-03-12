from rest_framework import serializers
from .models import Venue, Audition

class VenueSerializer(serializers.HyperlinkedModelSerializer):
    auditions = serializers.HyperlinkedRelatedField(
        view_name='audition_detail',
        many=True,
        read_only=True
    )
    class Meta:
       model = Venue
       fields = ('id', 'name', 'website_url', 'auditions',)


class AuditionSerializer(serializers.HyperlinkedModelSerializer):
    venue = serializers.HyperlinkedRelatedField(
        view_name='venue_detail',
        read_only=True
    )
    class Meta:
       model = Audition
       fields = ('id','title', 'description', 'roles', 'date', 'time', 'location','venue')  