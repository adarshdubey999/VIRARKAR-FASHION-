from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from .models import Product, Review, Category


def product_list(request):

    products = Product.objects.all()
    categories = Category.objects.all()

    # -------------------------
    # Search
    # -------------------------
    query = request.GET.get("q")

    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )

    # -------------------------
    # Category Filter
    # -------------------------
    category = request.GET.get("category")

    if category:
        products = products.filter(category__slug=category)

    # -------------------------
    # Price Range Filter
    # -------------------------
    min_price = request.GET.get("min_price")
    max_price = request.GET.get("max_price")

    if min_price:
        products = products.filter(price__gte=min_price)

    if max_price:
        products = products.filter(price__lte=max_price)

    # -------------------------
    # Sorting
    # -------------------------
    sort = request.GET.get("sort")

    if sort == "low":
        products = products.order_by("price")

    elif sort == "high":
        products = products.order_by("-price")

    elif sort == "new":
        products = products.order_by("-id")

    elif sort == "az":
        products = products.order_by("name")

    return render(request, "product_list.html", {
        "products": products,
        "categories": categories,
        "query": query,
    })


@login_required
def add_review(request, slug):

    product = get_object_or_404(Product, slug=slug)

    existing_review = Review.objects.filter(
        product=product,
        user=request.user
    ).exists()


    if existing_review:

        messages.warning(
            request,
            "You can give a review only once for this product."
        )

        return redirect(
            "product_detail",
            slug=product.slug
        )


    if request.method == "POST":

        rating = request.POST.get("rating")
        comment = request.POST.get("comment")


        Review.objects.create(
            product=product,
            user=request.user,
            rating=rating,
            comment=comment
        )


        messages.success(
            request,
            "Your review has been submitted successfully."
        )


    return redirect(
        "product_detail",
        slug=product.slug
    )



def product_detail(request, slug):

    product = get_object_or_404(Product, slug=slug)

    reviews = product.reviews.all()


    total_reviews = reviews.count()


    if total_reviews > 0:

        average_rating = (
            sum(int(review.rating) for review in reviews)
            / total_reviews
        )

    else:

        average_rating = 0


    return render(request, "product_detail.html", {

        "product": product,
        "reviews": reviews,
        "average_rating": average_rating,
        "total_reviews": total_reviews,

    })