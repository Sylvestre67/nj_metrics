__author__ = 'Sylvestre'
from metrics.models import County,Election,Party
from random import randint
import datetime
import radar

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
        object2.name = 'DEMOCRAT'
        object2.code = 'DEM'
        object2.election = election
        object2.number = 250000
        object2.save()

        return Election.objects.all()

c = create_counties()
county = c[0]
e = create_elections(county)
election = e[0]
create_parties(election)

election = e[1]
create_parties(election)

election = e[2]
create_parties(election)
