from django.shortcuts import render,render_to_response,RequestContext,HttpResponse
from django.core import serializers
from metrics import models
import json
import csv
from django.http import JsonResponse
from django.core.urlresolvers import reverse


def write_csv_data_feed(queryset, response):
    #Write the CSV header
    writer = csv.writer(response)
    writer.writerow(['category','column-1'])
    #Inititate next row
    row = []
    #Populate next row
    for c in queryset:
        row.append(c.name)
        row.append(c.number)
        writer.writerow(row)
        row=[]

# Create your views here.
def index(request):
    context = RequestContext(request)
    data_url = (reverse('counties_csv'))

    counties = models.County.objects.all()

    return render_to_response('index.html',{'data_url' : data_url, 'counties' : counties} , context)

def counties_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    data = models.County.objects.all()

    write_csv_data_feed(data,response)

    return response

def votes_year_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachement; filename="data.csv"'

    elections = models.Election.objects.all()
    data = models.get_voters_per_year(elections)

    #Write the CSV header
    writer = csv.writer(response)
    writer.writerow(['category','column-1'])
    #Inititate next row
    row = []
    #Populate next row
    for c in data:
        row.append(c)
        row.append(data[c])
        writer.writerow(row)
        row=[]

    return response

def votes_year_csv_county(request,countyId):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachement; filename="data.csv"'

    county = models.County.objects.get(id = countyId )

    elections = models.Election.objects.filter(county = county)
    data = models.get_voters_per_year(elections)

    #Write the CSV header
    writer = csv.writer(response)
    writer.writerow(['category','column-1'])
    #Inititate next row
    row = []
    #Populate next row
    for c in data:
        row.append(c)
        row.append(data[c])
        writer.writerow(row)
        row=[]

    return response

def votes_party_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachement; filename="data.csv"'

    parties = models.Party.objects.all()
    data = []

    #Write the CSV header
    writer = csv.writer(response)
    writer.writerow(['category','column-1'])
    #Inititate next row
    row = []
    #Populate next row
    for c in data:
        row.append(c)
        row.append(data[c])
        writer.writerow(row)
        row=[]

    return response


def party_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    data = models.Party.objects.all()

    write_csv_data_feed(data,response)

    return response
