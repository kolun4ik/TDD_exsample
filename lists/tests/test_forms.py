from django.test import TestCase
from lists.forms import ItemForm

class ItemFormTest(TestCase):
    """тест формы для элемента списка"""

    def test_fotm_item_input_has_placeholder_and_css_classes(self):
        """тест: поле ввода имеет атрибут placeholder и css слассы"""
        form = ItemForm()
        self.assertIn('placeholder="Enter to-do item"', form.as_p())
        self.assertIn('class="form-control input-lg"', form.as_p())