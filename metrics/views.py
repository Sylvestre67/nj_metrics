from django.shortcuts import render,render_to_response,RequestContext
from django.core import serializers
from metrics import models

# Create your views here.
def index(request):
    context = RequestContext(request)
    return render_to_response('index.html', {}, context)

def counties_JSON(request):
    context = RequestContext
    data = serializers.serialize("json", models.County.objects.all())
    return data

