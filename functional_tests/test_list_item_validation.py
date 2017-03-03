from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty input box
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys(Keys.RETURN)

        # The home page refreshes, and there is an error message saying
        # that list items cannot be blank.
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # She tries again with some text for the item, which now works.
        form_field = self.get_item_input_box()
        form_field.send_keys('Buy milk')
        form_field.send_keys(Keys.RETURN)
        self.check_for_row_in_list_table('1: Buy milk')
        time.sleep(2)

        # Perversely, she now decides to submit a second blank list item.
        self.get_item_input_box().send_keys(Keys.RETURN)
        time.sleep(4)

        # She receives a similar warning on the list page.
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # And she can correct it by filling some text in
        form_field = self.get_item_input_box()
        form_field.send_keys('Make tea')
        form_field.send_keys(Keys.RETURN)
        time.sleep(2)

        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')

    def test_cannot_add_duplicate_items(self):
        # Edith goes to the home page and starts a new list
        self.browser.get(self.server_url)
        form_field = self.get_item_input_box()
        form_field.send_keys('Buy wellies\n')
        form_field.send_keys(Keys.RETURN)
        self.check_for_row_in_list_table('1: Buy wellies')

        # She accidentally tries to enter a duplicate item
        self.get_item_input_box().send_keys('Buy wellies\n')

        # She sees a helpful error message
        form_field = self.get_item_input_box()
        form_field.send_keys('Buy wellies\n')
        form_field.send_keys(Keys.RETURN)
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You've already got this in your list")
