from django.test import TestCase
from .models import Item

class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        item = Item.objects.create(name='Test todo Item', done=False)
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        item = Item.objects.create(name='Test todo Item', done=False)
        self.assertEqual(str(item), 'Test todo Item')
