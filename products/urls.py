from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.categories_list, name='categories_list'),
    path('categories/<str:category_id>/', views.products_by_category, name='products_by_category'),
]
