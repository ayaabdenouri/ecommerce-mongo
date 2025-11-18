# products/management/commands/populate_products.py
from django.core.management.base import BaseCommand
from products.models import Product, Category
import random

class Command(BaseCommand):
    help = "Remplit la base avec des produits test"

    def handle(self, *args, **kwargs):
        categories = ["Électronique", "Vêtements", "Maison", "Sport", "Livres"]
        cat_objs = [Category.objects.get_or_create(name=c)[0] for c in categories]

        for i in range(1, 101):
            Product.objects.create(
                name=f"Produit {i}",
                description=f"Description du produit {i}",
                price=round(random.uniform(10, 500), 2),
                stock=random.randint(0, 100),
                category=random.choice(cat_objs),
                image_url="https://via.placeholder.com/150"
            )
        self.stdout.write(self.style.SUCCESS("100 produits créés !"))
