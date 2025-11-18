from django.core.management.base import BaseCommand
from products.models import Category

class Command(BaseCommand):
    help = "Créer les catégories par défaut"

    def handle(self, *args, **kwargs):
        categories = ["Électronique", "Vêtements", "Maison", "Sport", "Livres"]
        for name in categories:
            cat, created = Category.objects.get_or_create(name=name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Catégorie "{name}" créée'))
            else:
                self.stdout.write(f'Catégorie "{name}" existe déjà')
