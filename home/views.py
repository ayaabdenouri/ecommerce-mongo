from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')

def user_page(request):
    return render(request, 'home/user.html')
