from django.shortcuts import render

from products.models import Product


def home(request):
    products = Product.objects.all()
    featured_products = Product.objects.all()[:3]

    return render(request, 'home.html', {
        'products': products,
        'featured_products': featured_products
    })