from django.core.management.base import BaseCommand
from listings.models import Listing
from faker import Faker
import random

fake = Faker()

class Command(BaseCommand):
    help = 'Seed the database with sample listings data.'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("Seeding database..."))

        # Clear existing records for clean seeding
        Listing.objects.all().delete()

        for _ in range(10):
            Listing.objects.create(
                name=fake.company(),
                description=fake.text(),
                location=fake.city(),
                price_per_night=round(random.uniform(50, 500), 2),
                available=random.choice([True, False])
            )

        self.stdout.write(self.style.SUCCESS("Database seeded successfully."))
