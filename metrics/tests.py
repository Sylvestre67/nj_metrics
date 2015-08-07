from django.test import TestCase
from django.core.urlresolvers import resolve,reverse
from django.http import HttpRequest
from django.template.loader import render_to_string

from metrics.views import index,counties_JSON
from metrics.models import Year, County, Party


def create_counties():
    first_county = County()
    first_county.name = 'GLOUCESTER'
    first_county.number = 250000
    first_county.save()

    second_county = County()
    second_county.name = 'ATLANTIC'
    second_county.number = 365000
    second_county.save()

    return County.objects.all()

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

    def test_index_view_can_query_all_model(self):
        request=HttpRequest
        response = index(request)



class ModelTest(TestCase):
    def test_can_save_year(self):
        first_year = Year()
        first_year.year = 2010
        first_year.number = 250000
        first_year.save()

        years = Year.objects.all()
        self.assertEqual(years.count(),1)

    def test_can_save_county(self):
        first_county = County()
        first_county.name = 'GLOUCESTER'
        first_county.number = 250000
        first_county.save()

        second_county = County()
        second_county.name = 'ATLANTIC'
        second_county.number = 365000
        second_county.save()

        total = first_county.number + second_county.number
        self.assertEqual(total,(250000 + 365000))

    def test_can_save_party(self):
        dem = Party()
        dem.name = 'Democratic Party'
        dem.number = 250000
        dem.save()

        rep = Party()
        rep.name = 'Republican Party'
        rep.number = 250000
        rep.save()

        parties = Party.objects.all()
        self.assertEqual(parties.count(), 2)



class SerializerModelTest(TestCase):

    def test_counties_url_serializer_view_resolve_to_JSON_file(self):
        found = resolve(reverse('counties_JSON'))
        self.assertEqual(found.func, counties_JSON)

    def test_JSON_counties_files_created(self):
        counties = create_counties()
        request = HttpRequest()
        response = counties_JSON(request)
        print('Response is: ')
        print(response)
        self.assertIn('metrics.county', response)






