import csv
import requests
from django.core.management.base import BaseCommand
from restaurants.models import Restaurant

class Command(BaseCommand):
    help = 'Load data from zomato.csv into the Restaurant model'

    def handle(self, *args, **options):
        file_path = '/Users/naveenm/Coding/placementDrives/task-MadugulaNaveen/zomato.csv'

        with open(file_path, newline='', encoding='ISO-8859-1') as csvfile:
            reader = csv.DictReader(csvfile)
            i = 0
            for row in reader:
                Restaurant.objects.create(
                    name=row['Restaurant Name'],
                    cuisine=row['Cuisines'],
                    city=row['City'],
                    address=row['Address'],
                    country_code=row['Country Code'],
                    rating=row['Aggregate rating'],
                    number_of_ratings=row['Votes'],
                    cost_for_two=row['Average Cost for two'],
                    image_url=row['image_url']
                )
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
