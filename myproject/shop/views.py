from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Product


def home(request):
    return render(request, 'shop/home.html')


def products(request):
    products = Product.objects.all()
    return render(request, 'shop/products.html', {'products': products})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'shop/register.html', {'form': form})