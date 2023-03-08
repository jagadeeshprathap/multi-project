from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first_app2(request):
    return HttpResponse("she is very inteligent")
def second_app2(request):
    return HttpResponse("this is second app")

