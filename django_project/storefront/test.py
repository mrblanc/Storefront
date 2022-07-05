from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from datetime import datetime

from .apps import StorefrontConfig
from .models import Product

class ProductModelTest(TestCase):

  def test_product(self):
    name = 'Banana'
    description = 'A radioactive yellow berry'
    date_added = datetime.min
    price = 123.44
    product = Product(name=name, description=description, date_added=date_added, price=price)
    self.assertIs(product.__str__(), name)

class AddProductViewTest(TestCase):

  def setUp(self):
    test_user = User.objects.create_user(username='test_user', password='1A2b3C4d!@')
    test_user.save()

  def test_redirect_if_not_logged_in(self):
    response = self.client.get(reverse('storefront:view_products'))
    self.assertRedirects(response, '/accounts/login/?next=/storefront/view_products/')

  def test_logged_in_user_uses_correct_template(self):
    login = self.client.login(username='test_user', password='1A2b3C4d!@')
    response = self.client.get(reverse('storefront:view_products'))

    # Verify user is logged in
    self.assertEqual(str(response.context['user']), 'test_user')
    # Check that we got a response "success"
    self.assertEqual(response.status_code, 200)

    # Verify correct template is used
    self.assertTemplateUsed(response, 'products/table.html')
