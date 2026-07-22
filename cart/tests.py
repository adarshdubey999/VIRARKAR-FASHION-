from django.test import TestCase
from django.urls import reverse

from products.models import Category, Product


class AddToCartViewTests(TestCase):
    def setUp(self):
        category = Category.objects.create(name='Shoes', slug='shoes')
        self.product = Product.objects.create(
            category=category,
            name='Running Shoe',
            slug='running-shoe',
            description='Comfortable running shoe',
            price='1999.00',
            image='',
            stock=10,
            available=True,
        )

    def test_add_to_cart_stores_product_in_session(self):
        response = self.client.post(reverse('add_to_cart', args=[self.product.slug]))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/cart/')

        cart = self.client.session.get('cart', {})
        self.assertIn(str(self.product.id), cart)
        self.assertEqual(cart[str(self.product.id)], 1)

    def test_decrease_quantity_removes_item_when_it_reaches_zero(self):
        session = self.client.session
        session['cart'] = {str(self.product.id): 1}
        session.save()

        response = self.client.post(reverse('decrease_quantity', args=[self.product.id]))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/cart/')

        cart = self.client.session.get('cart', {})
        self.assertNotIn(str(self.product.id), cart)
