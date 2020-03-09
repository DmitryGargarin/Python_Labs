from django.http import HttpResponse
from django.shortcuts import render
from .models import User

# Create your views here.


def index(request):
    data = {"header": "Header", "users": User.objects.order_by('Name')[:5]}
    return render(request, "index.html", context=data)