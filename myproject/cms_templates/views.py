from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from models import cars
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.template import Context

# Create your views here.

def login(request):
    if request.user.is_authenticated():
        return (" " + request.user.username)
    else:
        return ("<br><br>You arent logged <a href='/admin/login/'>Login</a><br>")

def all(request):
    cars_list = cars.objects.all()
    out = "<ul>\n"
    for fila in cars_list:
        out += "<li><a href=anotated/" + fila.model +  " > " + fila.model + "</a></li>\n"
    out += "</ul\n"
    out += login(request)
    return HttpResponse(out)

@csrf_exempt
def show (request, resource):
    if request.method == 'GET':        
        out = ""
        try:
            one_car = cars.objects.get(model = resource)
            out += one_car.model + ": " + str(one_car.price) + "$"
        except:
            out += "Car not found, add to DB"
        out += login(request)
        return HttpResponse(out)
    elif request.method == 'PUT':
        if request.user.is_authenticated():
            newCar = cars(model = resource, price = request.body)
            newCar.save()
            out = "Saved"
        else:
            out = "You arent logged"
    out += login (request)
    return HttpResponse (out)

def showtemplate (request, resource):
    #DRY!
    out = ""
    try:
        one_car = cars.objects.get(model = resource)
        out += one_car.model + ": " + str(one_car.price) + "$"        
    except:
        out += "Car not found, add to DB"
    #Template
    template = get_template ("index.html")
    c = Context ({'stuff': out})
    render = template.render(c)
    return HttpResponse(render)


def notfound (request, resource):
    out = ("404 Not found: " + resource)
    out += login(request)
    return HttpResponseNotFound(out)
