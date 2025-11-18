from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Liste des catégories
def categories(request):
    all_categories = Category.objects.all()
    return render(request, 'products/categories.html', {'categories': all_categories})

# Produits par catégorie
def products_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'products/products_by_category.html', {
        'category': category,
        'products': products
    })
