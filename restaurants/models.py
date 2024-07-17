from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.TextField()
    country_code = models.IntegerField()
    rating = models.FloatField()
    number_of_ratings = models.IntegerField()
    cost_for_two = models.IntegerField()

    def __str__(self):
        return self.name
