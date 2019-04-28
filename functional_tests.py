from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    """Тест нового пользовтеля"""

    def setUp(self):
        """Установка"""
        self.browser = webdriver.Firefox()

    def tearDown(self):
        """Демонтаж"""
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        """Тест: можно начать списко и получить его позже"""
        # Эдит слышала про крутое новое он-лайн приложение со списком
        # неотложных дел. Она решает оценить его домашнбб страницу.
        self.browser.get('http://localhost:8000/')

        # Она видит, что заголовок и шапка страницы говорят о списках
        # неотложных дел.
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Ей сражу же предлагается ввести элемент списка
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter To-Do item'
        )
        # Она набирает в текстовом поле "Купить павлиньи перья" (ее хобби-
        # вязание рыболовных мушек)
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: купить павлиньи перья' for row in rows),
            "Новый элемент списка не появился в таблице!"
        )
        # Когда она нажимает enter, страница обновляется, и теперь страница
        # содержит "1. Купить павлиньи перья" в качестве элемента списка.

        # Текстовое поле по прежнему предлагает добавить еще один элемент.
        # Она вводит "Сделать мушку из павлиньих перьев"
        # (Эдит очень методична)
        self.fail('Закончить тест.')

        # Страница снова обновляется, и, теперь, показывает оба элемента ее списка.

        # Эдит интересно, запомнил ли сайт ее список. Далее она видит, что сайт
        # сгенерировал для нее уникальный URL-адрес, об этом выводиться небольшой
        # текст с обьяснениями.

        # Она посещает этот URL-адрес - ее список по прежнему там.

        # Удовлетворенная, она ложиться спать.

if __name__ == "__main":
    unittest.main(warnings='ignore')

