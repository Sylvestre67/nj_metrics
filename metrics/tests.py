from django.test import TestCase
from django.core.urlresolvers import resolve,reverse
from django.http import HttpRequest
from django.template.loader import render_to_string

from metrics.views import index,counties_csv,party_csv,votes_year_csv,votes_year_csv_county,votes_party_csv
from metrics.models import Election, County, Party, number_of_votes,number_of_vote_per_year,get_voters_per_year,get_number_of_vote_per_party_per_election,get_number_of_vote_per_party_per_election_per_county

from random import randint
import datetime
import radar

def create_objects(Object):
    for i in range(1,5,1):
        object = Object()
        object.name = str(randint(2008,2020))
        object.number = randint(250000, 450000)
        object.save()

    return Object.objects.all()

def create_counties():
    for i in range(1,5,1):
        object = County()
        object.name = str(randint(2008,2020))
        object.number = randint(250000, 450000)
        object.save()

    return County.objects.all()

def create_elections(county):
    for i in range(1,5,1):
        object = Election()
        object.name = str(randint(2008,2020))
        object.date = radar.random_datetime()
        object.county = county
        object.save()

    return Election.objects.all()

def create_parties(election):
        object = Party()
        object.name = 'DEMOCRAT'
        object.code = 'DEM'
        object.election = election
        object.number = 250000
        object.save()

        object2 = Party()
        object2.name = 'REPUBLICAN'
        object2.code = 'REP'
        object2.election = election
        object2.number = 250000
        object2.save()

        return Party.objects.all()


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

     def test_can_save_election(self):
        c = create_counties()
        election = Election()
        election.name = 'FIRE ELECTION'
        election.date = datetime.date.today()
        election.county = c[0]
        election.save()

        election = Election()
        election.name = '"2006 MUNICIPAL"'
        election.county = c[0]
        election.save()

        elections = Election.objects.all()
        self.assertEqual(elections.count(), 2)

     def test_can_save_party(self):
        c = create_counties()
        e = create_elections(c[0])
        first_party = Party()
        first_party.code = 'DEM'
        first_party.name = 'Democrat'
        first_party.number = 250000
        first_party.county = c[0]
        first_party.election = e[0]
        first_party.save()

        parties = Party.objects.all()
        self.assertEqual(parties.count(),1)

     def test_can_count_number_of_votes_per_elections(self):
        c = create_counties()
        e = create_elections(c[0])
        p = create_parties(e[0])
        n =number_of_votes( e[0])
        self.assertEqual(n,500000)

     def test_can_retrieve_the_number_of_votes_for_a_specific_year(self):
        c = create_counties()
        e = create_elections(c[0])
        p = create_parties(e[0])

        year = e[0].date.year
        n_year = number_of_vote_per_year(year)

        self.assertEqual(n_year,500000)

     def test_can_create_a_dictionary_with_all_years_and_their_corresponding_number_of_vote(self):
        c = create_counties()
        e = create_elections(c[0])
        p = create_parties(e[0])

        data = get_voters_per_year(e)
        self.assertIn(e[0].date.year, data.keys())
        self.assertEqual(number_of_vote_per_year(e[0].date.year), data[e[0].date.year])

     def test_can_calculate_the_total_number_of_votes_per_party(self):
        c = create_counties()
        e = create_elections(c[0])
        p = create_parties(e[0])

        n = get_number_of_vote_per_party_per_election(e[0])

        self.assertEqual(n[p[0].name], 250000)

     def get_number_of_vote_per_party_per_election_per_county(self):
        c = create_counties()
        e = create_elections(c[0])
        p = create_parties(e[0])

        n = get_number_of_vote_per_party_per_election_per_county(e[0],c[0])

        self.assertEqual(n[p[0].name], 250000)

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

    def test_votes_year_csv_url_serializer_view_resolve_to_csv_file(self):
        self.url_resolve_to_view('votes_year_csv',votes_year_csv)

    def test_votes_year_csv_view_generates_csv_file(self):
        c = create_counties()
        e = create_elections(c[0])
        p = create_parties(e[0])

        self.view_generates_csv_file(votes_year_csv)

    def test_votes_and_years_in_csv_file(self):
        c = create_counties()
        e = create_elections(c[0])
        p = create_parties(e[0])

        election_year = str(e[0].date.year)

        request = HttpRequest()
        response = votes_year_csv(request)
        print(response.content)
        self.assertIn(election_year, response.content.decode())

    def test_votes_year_csv_county_url_serializer_view_resolve_to_csv_file(self):
        c = create_counties()
        print(reverse(votes_year_csv_county, args = [c[0].id]))

        found = resolve(reverse(votes_year_csv_county, args = [c[0].id]))
        self.assertEqual(found.func, votes_year_csv_county)

    def test_votes_year_csv_county_view_generates_csv_file(self):
        c = create_counties()
        e = create_elections(c[0])
        p = create_parties(e[0])

        request = HttpRequest()
        response = votes_year_csv_county(request, c[0].id)
        self.assertEqual('text/csv', response._headers['content-type'][1])

    def test_number_per_year_are_filtered_per_county(self):
        c = create_counties()
        e = create_elections(c[0])
        p = create_parties(e[0])

        request = HttpRequest()
        response = votes_year_csv_county(request, c[0].id)

        elections = Election.objects.filter(county = c[0])
        data = get_voters_per_year(elections)

        self.assertIn(str(data[elections[0].date.year]), response.content.decode())

    def test_votes_per_party_resolve_to_a_view(self):
        self.url_resolve_to_view('votes_party_csv',votes_party_csv)

    def test_votes_per_party_generate_csv(self):
        c = create_counties()
        e = create_elections(c[0])
        p = create_parties(e[0])

        request = HttpRequest()
        response = votes_party_csv(request)
        self.assertEqual('text/csv', response._headers['content-type'][1])


    def test_votes_per_party_contains_party_and_votes(self):
        c = create_counties()
        e = create_elections(c[0])
        p = create_parties(e[0])

        party_name = str(p[0].name)

        request = HttpRequest()
        response = votes_party_csv(request)
        print(response.content)

        self.assertIn(party_name, response.content.decode())