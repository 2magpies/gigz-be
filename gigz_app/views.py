from rest_framework import generics
from .serializers import VenueSerializer, AuditionSerializer
from .models import Venue, Audition

# For GET and CREATE venue(s)
class VenueList(generics.ListCreateAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

# Retrieve, Update, Delete venue
class VenueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

# For GET and CREATE audition(s)
class AuditionList(generics.ListCreateAPIView):
    queryset = Audition.objects.all()
    serializer_class = AuditionSerializer

# Retrieve, Update, Delete audition
class AuditionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Audition.objects.all()
    serializer_class = AuditionSerializer