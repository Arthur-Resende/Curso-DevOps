from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('render/index.html')
    context = {
        "titulo": "Atividade django",
        "descricao": "template bootstrap renderizado com django"
    }
    return HttpResponse(template.render(context, request))
