from django.shortcuts import render
from django.http import HttpResponse


def nova_empresa(request):
    return HttpResponse('Estou em uma nova empresa')

    