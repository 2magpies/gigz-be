from django.db import models

# Create your models here.
class Venue(models.Model):
    name = models.TextField()
    website_url = models.TextField()

    def __str__(self):
        return self.name

       

class Audition(models.Model):
    title = models.TextField()
    description = models.TextField()
    roles = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.TextField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='auditions')
    
    def __str__(self):
        return self.title