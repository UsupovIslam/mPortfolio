from django.shortcuts import render
from django.http import HttpResponse

from .models import MyPort


def index(request):
    my_car = MyPort.objects.all()
    data = {
        'my_port_list': my_car
    }

    return render(request, 'index.html', data)
