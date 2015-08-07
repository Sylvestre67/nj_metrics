from django.test import TestCase
from django.core.urlresolvers import resolve,reverse
from django.http import HttpRequest
from django.template.loader import render_to_string

from metrics.views import index,counties_csv,years_csv,party_csv
from metrics.models import Year, County, Party

from random import randint

def create_objects(Object):
    for i in range(1,5,1):
        object = Object()
        object.name = str(randint(2008,2020))
        object.number = randint(250000, 450000)
        object.save()

    return Object.objects.all()



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

    def url_resolve_to_view(self,url_name,view):
        found = resolve(reverse(url_name))
        self.assertEqual(found.func, view)

    def view_generates_csv_file(self,view):
        request = HttpRequest()
        response = view(request)
        self.assertEqual('text/csv', response._headers['content-type'][1])

    def object_in_csv(self,view,object):
        request = HttpRequest()
        response = counties_csv(request)
        self.assertIn(object, response.content.decode())

    def test_counties_url_serializer_view_resolve_to_csv_file(self):
        self.url_resolve_to_view('counties_csv',counties_csv)

    def test_csv_counties_view_generates_csv_file(self):
        counties = create_objects(County)
        request = HttpRequest()
        response = counties_csv(request)
        self.assertEqual('text/csv', response._headers['content-type'][1])

    def test_csv_counties_in_csv_file(self):
        counties = create_objects(County)
        first_counties_name = County.objects.all()[0].name
        request = HttpRequest()
        response = counties_csv(request)
        self.assertIn(first_counties_name, response.content.decode())

    def test_year_url_serializer_view_resolve_to_csv_file(self):
        self.url_resolve_to_view('years_csv',years_csv)

    def test_csv_years_view_generates_csv_file(self):
        counties = create_objects(Year)
        self.view_generates_csv_file(years_csv)

    def test_years_in_csv_file(self):
        years = create_objects(Year)
        first_years_name = Year.objects.all()[0].name
        request = HttpRequest()
        response = years_csv(request)
        self.assertIn(first_years_name, response.content.decode())

    def test_party_url_serializer_view_resolve_to_csv_file(self):
        self.url_resolve_to_view('party_csv',party_csv)

    def test_csv_party_view_generates_csv_file(self):
        counties = create_objects(Party)
        self.view_generates_csv_file(counties_csv)

    def test_party_in_csv_file(self):
        counties = create_objects(Party)
        first_party_name = Party.objects.all()[0].name
        request = HttpRequest()
        response = party_csv(request)
        print(response.content)
        self.assertIn(first_party_name, response.content.decode())










