__author__ = 'Sylvestre'

from selenium import webdriver
from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_visit_home_page_and_see_NJ_metrics(self):
        #Jimi heard about this great collection of data and metrics about New-Jersey Voting history.
        #He goes and check this great website
        self.browser.get(self.live_server_url)

        #He notices the title of the webiste "New Jersey Voters Metrics', and the header inviting him to discover all the great stuff we cooked for him.
        self.assertIn('New Jersey Voters Metrics', self.browser.title)
        title = self.browser.find_element_by_tag_name('h1')
        self.assertIn('A collection of metrics', title.text)




        self.fail('Finish the test!')
