from products.models import Category, Product

catalog = {
    "shirts": {
        "name": "Shirts",
        "products": [
            {
                "name": "Oxford Essential Shirt",
                "slug": "oxford-essential-shirt",
                "description": "A polished Oxford shirt with a comfortable everyday fit.",
                "price": "1299.00",
                "stock": 18,
                "image": "products/catalog-shirt.svg",
            },
            {
                "name": "Crisp Linen Shirt",
                "slug": "crisp-linen-shirt",
                "description": "Lightweight linen texture for effortless warm-weather style.",
                "price": "1499.00",
                "stock": 14,
                "image": "products/catalog-shirt.svg",
            },
        ],
    },
    "pants": {
        "name": "Pants",
        "products": [
            {
                "name": "Relaxed Fit Pants",
                "slug": "relaxed-fit-pants",
                "description": "An easy relaxed fit designed for comfortable daily movement.",
                "price": "1599.00",
                "stock": 16,
                "image": "products/catalog-pants.svg",
            },
            {
                "name": "Everyday Cotton Pants",
                "slug": "everyday-cotton-pants",
                "description": "Soft cotton pants with a clean silhouette for daily wear.",
                "price": "1399.00",
                "stock": 20,
                "image": "products/catalog-pants.svg",
            },
        ],
    },
    "t-shirts": {
        "name": "T-shirts",
        "products": [
            {
                "name": "Essential Crew T-shirt",
                "slug": "essential-crew-tshirt",
                "description": "A versatile crew-neck T-shirt made for everyday comfort.",
                "price": "699.00",
                "stock": 30,
                "image": "products/catalog-tshirt.svg",
            },
            {
                "name": "Premium Oversized T-shirt",
                "slug": "premium-oversized-tshirt",
                "description": "A modern oversized shape with a premium soft-touch finish.",
                "price": "899.00",
                "stock": 24,
                "image": "products/catalog-tshirt.svg",
            },
        ],
    },
    "trousers": {
        "name": "Trousers",
        "products": [
            {
                "name": "Tailored Formal Trousers",
                "slug": "tailored-formal-trousers",
                "description": "Sharp tailored trousers for polished office and occasion looks.",
                "price": "1899.00",
                "stock": 12,
                "image": "products/catalog-trousers.svg",
            },
            {
                "name": "Straight Leg Trousers",
                "slug": "straight-leg-trousers",
                "description": "A timeless straight-leg cut that works from desk to dinner.",
                "price": "1699.00",
                "stock": 15,
                "image": "products/catalog-trousers.svg",
            },
        ],
    },
}

for category_slug, category_data in catalog.items():
    category, _ = Category.objects.update_or_create(
        slug=category_slug,
        defaults={"name": category_data["name"]},
    )
    for product_data in category_data["products"]:
        Product.objects.update_or_create(
            slug=product_data["slug"],
            defaults={
                **product_data,
                "category": category,
                "available": True,
            },
        )

print("Seeded 8 men’s catalog products across Shirts, Pants, T-shirts, and Trousers.")
