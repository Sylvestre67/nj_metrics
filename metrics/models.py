from django.db import models
import datetime

# Create your models here.

def number_of_votes(election):
        p = Party.objects.filter(election = election)
        n = 0
        for party in p:
            n += party.number

        return n

def number_of_vote_per_year(year):
    e = Election.objects.filter(date__year = year)
    total = 0

    for election in e:
        total += number_of_votes(election)
    return total

def get_number_of_vote_per_party_per_election(election):
    votes = Party.objects.filter(election = election)
    results = dict()

    for v in votes:
        results[v.name] = v.number
    print(results)

    return results

def get_number_of_vote_per_party_per_election_per_county(election,county):
    votes = Party.objects.filter(election = election, county = county)
    results = dict()

    for v in votes:
        results[v.name] = v.number
    print(results)

    return results


def get_voters_per_year(elections):
    list_of_years = list()

    for e in elections:
        if not e.date.year in list_of_years:
            list_of_years.append(e.date.year)

    value = dict()
    for year in list_of_years:
        value[year] = number_of_vote_per_year(year)

    return value


class County(models.Model):
    name = models.CharField(max_length = 255)
    number = models.IntegerField()

    def __str__(self):
        return self.name

class Election(models.Model):
    county = models.ForeignKey(County)
    name = models.CharField(max_length=255)
    date = models.DateField(null = True)

    def __str__(self):
        return  self.county.name + " " + self.name

class Party(models.Model):
    election = models.ForeignKey(Election)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=3,null=True)
    number = models.BigIntegerField(default=0)

    def __str__(self):
        return self.election.county.name + " " +  self.election.name + " " +  self.name