from django.shortcuts import redirect, render, get_object_or_404
from products.models import Product


def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)

    # Prevent adding unavailable products
    if not product.available or product.stock <= 0:
        return redirect("product_detail", slug=product.slug)

    cart = request.session.get('cart', {})
    product_id = str(product.id)

    current_quantity = cart.get(product_id, 0)

    # Increase only if stock is available
    if current_quantity < product.stock:
        cart[product_id] = current_quantity + 1

    request.session['cart'] = cart

    return redirect('view_cart')


def view_cart(request):
    cart = request.session.get('cart', {})

    items = []
    total = 0

    for product_id, qty in cart.items():

        product = get_object_or_404(Product, id=product_id)

        item_total = product.price * qty
        total += item_total

        items.append({
            'product': product,
            'quantity': qty,
            'item_total': item_total,
        })

    context = {
        'items': items,
        'total': total,
    }

    return render(request, 'cart.html', context)


def increase_quantity(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    cart = request.session.get('cart', {})

    product_key = str(product.id)

    current_quantity = cart.get(product_key, 0)

    # Increase quantity only if stock available
    if current_quantity < product.stock:
        cart[product_key] = current_quantity + 1

    request.session['cart'] = cart

    return redirect('view_cart')


def decrease_quantity(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    cart = request.session.get('cart', {})

    product_key = str(product.id)

    if product_key in cart:

        cart[product_key] = cart[product_key] - 1

        if cart[product_key] <= 0:
            del cart[product_key]

    request.session['cart'] = cart

    return redirect('view_cart')


def remove_from_cart(request, product_id):

    cart = request.session.get('cart', {})

    product_key = str(product_id)

    if product_key in cart:
        del cart[product_key]

    request.session['cart'] = cart

    return redirect('view_cart')