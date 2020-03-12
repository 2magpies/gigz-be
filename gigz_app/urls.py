from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('venues/', views.VenueList.as_view(), name='venue_list'),
    path('venues/<int:pk>', views.VenueDetail.as_view(), name='venue_detail'),
    path('auditions/', views.AuditionList.as_view(), name="audition_list"),
    path('auditions/<int:pk>', views.AuditionDetail.as_view(), name="audition_detail"),
    
    
    

]