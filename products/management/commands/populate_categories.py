from django.core.management.base import BaseCommand
from products.models import Category

class Command(BaseCommand):
    help = "Populate default product categories"

    def handle(self, *args, **options):
        categories = ["Électronique", "Vêtements", "Maison", "Sport", "Livres"]
        for name in categories:
            Category.objects.get_or_create(name=name)
        self.stdout.write(self.style.SUCCESS("Categories populated successfully!"))
