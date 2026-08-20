from django.shortcuts import render

from products.models import Product


def home(request):
    products = Product.objects.exclude(category__slug__icontains="women")
    featured_products = products[:3]

    return render(request, 'home.html', {
        'products': products,
        'featured_products': featured_products
    })