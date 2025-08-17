from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth import get_user_model
import random

User = get_user_model()

class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        host, _ = User.objects.get_or_create(
            email="host@example.com",
            defaults={"username": "hostuser", "first_name": "Host", "last_name": "User", "password": "hostpass"}
        )

        for i in range(10):
            Listing.objects.create(
                title=f"Cozy Home {i}",
                description="A beautiful home perfect for vacations.",
                price_per_night=random.randint(50, 200),
                location=f"City {i}",
                host=host,
            )
        self.stdout.write(self.style.SUCCESS("Successfully seeded listings."))
