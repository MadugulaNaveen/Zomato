from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=100)
    address = models.TextField()
    country_code = models.IntegerField()
    rating = models.FloatField(null=True)
    number_of_ratings = models.IntegerField(null=True)
    cost_for_two = models.IntegerField(null=True)
    image_url = models.URLField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.name
