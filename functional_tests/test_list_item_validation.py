from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    """тест валидации элемента списка"""

    def test_cannot_add_empty_list_items(self):
        """тест: нельзя добавить пустые элементы списка"""
        # Эдит открываеи домашнюю страницу и пытается отправить
        # пустой элемент списка. Она нажимает Enter на пустом поле
        # ввода.
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        # Браузер перехвативает запрос и не загружает страницу со списком
        self.wait_for(lambda: self.browser.find_elements_by_css_selector('#id_text:invalid'))

        # Эдит начинает набирать текст новго элемента и ошибка исчезает
        self.get_item_input_box().send_keys('Buy milk')
        self.wait_for(lambda: self.browser.find_elements_by_css_selector('#id_text:valid'))

        # И она может отправить его успешно
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Как нт странно, Эдит пытается отправить второй пустой элемент списка
        self.get_item_input_box().send_keys(Keys.ENTER)

        # И снова браузер не подчиняется
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for(lambda: self.browser.find_elements_by_css_selector('#id_text:invalid'))

        # И она сможет исправиться, заполнив поле текстом
        self.get_item_input_box().send_keys('Make tea')
        self.wait_for(lambda: self.browser.find_elements_by_css_selector('#id_text:valid'))
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')

    def test_cannot_add_duplicate_item(self):
        """тест: нельзя добавлять повторяющиеся элементы"""
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys('Buy wellies')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy wellies')

        # Она случайно пытаеться ввести повторяющийся элемент
        self.get_item_input_box().send_keys('Buy wellies')
        self.get_item_input_box().send_keys(Keys.ENTER)

        # Она видит полезное сообщение об ошибке
        self.wait_for(lambda: self.assertEqual(
                                    self.browser.find_element_by_css_selector('.has-error').text,
                                    "You`ve already got this in your list"
        ))
