from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from products.models import Product
from .models import Order, OrderItem


@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by("-created_at")

    return render(request, "orders/my_orders.html", {
        "orders": orders
    })


@login_required
def order_detail(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)

    return render(request, "orders/order_detail.html", {
        "order": order
    })


def checkout(request):
    cart = request.session.get("cart", {})

    cart_items = []
    total = 0

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)

        subtotal = product.price * quantity
        total += subtotal

        cart_items.append({
            "product": product,
            "quantity": quantity,
            "subtotal": subtotal,
        })

    if request.method == "POST":

        # Check stock before placing order
        for item in cart_items:
            product = item["product"]
            quantity = item["quantity"]

            if quantity > product.stock:
                return render(request, "orders/checkout.html", {
                    "cart_items": cart_items,
                    "total": total,
                    "error": f"Only {product.stock} item(s) of {product.name} are available."
                })

        order = Order.objects.create(
            user=request.user if request.user.is_authenticated else None,
            full_name=request.POST.get("full_name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            address=request.POST.get("address"),
            city=request.POST.get("city"),
            pincode=request.POST.get("pincode"),
            total_price=total,
            payment_method=request.POST.get("payment_method"),
        )

        for item in cart_items:
            product = item["product"]
            quantity = item["quantity"]

            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=product.price,
            )

            # Reduce stock
            product.stock -= quantity

            # Make product unavailable if stock becomes 0
            if product.stock <= 0:
                product.stock = 0
                product.available = False

            product.save()

        # Clear cart
        request.session["cart"] = {}

        return redirect("order_success")

    return render(request, "orders/checkout.html", {
        "cart_items": cart_items,
        "total": total,
    })


def order_success(request):
    return render(request, "orders/order_success.html")