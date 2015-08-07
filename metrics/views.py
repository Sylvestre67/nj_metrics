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
    return render_to_response('index.html',{'data_url' : data_url} , context)

def counties_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    data = models.County.objects.all()

    write_csv_data_feed(data,response)

    return response

def years_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'
    data = models.Year.objects.all()
    write_csv_data_feed(data,response)

    return response

def party_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    data = models.Party.objects.all()

    write_csv_data_feed(data,response)

    return response