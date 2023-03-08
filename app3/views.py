from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first_app3(request):
    return HttpResponse("this is first app3")
def second_app3(request):
    return HttpResponse("this is second app3")