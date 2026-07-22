from django.test import TestCase


class HomepageTests(TestCase):
    def test_homepage_renders_storefront_content(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Virarkar Fashion')
        self.assertContains(response, 'Shop Now')
