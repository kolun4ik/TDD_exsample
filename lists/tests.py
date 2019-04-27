from django.urls import resolve
from django.test import TestCase
from lists.views import home_page

class HomePageTest(TestCase):
    """тест домашней страницы"""

    def test_root_url_resolve_to_home_page_view(self):
        """тест: корневой Url преобразуется в представлеие
        домашней страницы"""
        found = resolve('/')
        self.assertEqual(found.func, home_page)
