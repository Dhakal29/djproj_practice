from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home.html')
    # return HttpResponse("Hello from home request of djproj ")


@csrf_exempt
def disp(request):
    val1 = request.POST['name']
    val2 = request.POST['gender']
    return render(request, "disp.html", {'result': val1})
