__author__ = 'Sylvestre'

from selenium import webdriver
from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    def test_can_visit_home_page_and_see_NJ_metrics(self):
        #Jimi heard about this great collection of data and metrics about New-Jersey Voting history.
        #He goes and check this great website
        self.browser.get(self.live_server_url)

        #He notices the title of the webiste "New Jersey Voters Metrics', and the header inviting him to discover all the great stuff we cooked for him.
        self.assertIn('New Jersey Voters Metrics', self.browser.title)
        title = self.browser.find_element_by_tag_name('h1')
        self.assertIn('A collection of New Jersey voters metrics', title.text)

        #He starts by exploring the first section of this home page, dedicated to the number of voters per county.
        chart = self.browser.find_element_by_class_name('v_p_c')
        self.assertEqual( "chartdiv", chart.get_attribute('id'))

        #He noticed a chart in this section.
        self.browser.find_element_by_css_selector('#chartdiv > .amcharts-main-div')

        #He scroll down a little bit further and keeps reading about the number of votes per yer.
        chart = self.browser.find_element_by_class_name('v_p_y')
        #He noticed a chart in this section.
        self.browser.find_element_by_css_selector('.v_p_y.amcharts-main-div')

        #He finally spend some time analyzing the pie chart on vote repartition per side (Democrate/Republicans/UNA)
        chart = self.browser.find_element_by_class_name('v_p_p')
        #He noticed a chart in this section.
        self.browser.find_element_by_css_selector('.v_p_p.amcharts-main-div')


        self.fail('Finish the test!')
