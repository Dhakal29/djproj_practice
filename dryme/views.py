from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
# Create your views here.


def index(request):
    dest1 = Destination()
    dest1.name = "Ipsum"
    return render(request, 'index.html', {'dest1': dest1})
    # return HttpResponse("Hello from home request of djproj ")
