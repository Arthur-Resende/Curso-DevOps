from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello world, voce esta no app render')

def verificador(request, arg_id):
    if arg_id <10:
        return HttpResponse(f"{arg_id} é menor que 10")
    else:
        return HttpResponse(f"{arg_id} é maior ou igual a 10")
