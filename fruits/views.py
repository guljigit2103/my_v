from django.shortcuts import render
from django.http import HttpResponse
from .models import Fruits


def index(request):
    fruits = Fruits.objects.all()
    return render(request, 'fruits.html', {'fruits': fruits})


