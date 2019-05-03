from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest


class ItemValodationTest(FunctionalTest):
    """тест валидации элемента списка"""

    def test_cannot_add_empty_list_item(self):
        """тест: нельзя добавить пустые элементы списка"""
        # Эдит открываеи домашнюю страницу и пытается отправить
        # пустой элемент списка. Она нажимает Enter на пустом поле
        # ввода.


        # Домашняя страница обновляется, и появляется сообщение об ошибке,
        # которое говорит, что элементы списка не должны быть пустыми


        # Она пробует снова, теперь с неким текстом для элемента, и теперь
        # это срабатывает
        # Как нт странно, Эдит пытается отправить второй пустой элемент списка


        # Она получает аналогичное предупреждение на странице списка


        # И она может его исправить, заполнив поле неким текстом

        self.fail("напиши меня")