from django.test import TestCase
from apps.store.models import Product
from apps.category.models import Category
from django.contrib.auth.models import User


class TestProduct(TestCase):

    def setUp(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.product = Product.objects.create(
            category_id=1, title='django', created_by_id=1, slug='django', price=20.00, image='example.jpg',  description='django details')

    def test_products_models(self):

        data = self.product
        self.assertEqual(str(data), 'django')
