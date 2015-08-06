from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from metrics.views import index
from django.template.loader import render_to_string

# Create your tests here.
class IndexViewTest(TestCase):

    def test_root_url_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_index_view_renders_template(self):
        request = HttpRequest()
        response = index(request)
        expected_html = render_to_string('../templates/index.html')
        self.assertEqual(response.content.decode(), expected_html)




