from django.test import TestCase
from apps.category.models import Category


class TestCategory(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model(self):
        '''Test category model data insertion/type/fields attributes '''
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_name(self):

        data = self.data1
        self.assertEqual(str(data), 'django')
