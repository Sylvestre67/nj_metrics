from django.shortcuts import render,render_to_response,RequestContext

# Create your views here.
def index(request):
    context = RequestContext(request)
    return render_to_response('index.html', {}, context)
