from django.shortcuts import render
from django.http import HttpResponse
from .models import Tecnologias, Empresa
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.contrib.messages import constants

def nova_empresa(request):
    if request.method == "GET":
        techs = Tecnologias.objects.all()
        return render(request, 'nova_empresa.html', {'techs': techs})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cidade = request.POST.get('cidade')
        endereco = request.POST.get('endereco')
        nicho = request.POST.get('nicho')
        caracteristicas = request.POST.get('caracteristicas')
        tecnologias = request.POST.getlist('tecnologias')
        logo = request.FILES.get('logo')
        
        if (len(nome.strip()) == 0 or len(email.strip()) == 0 or len(cidade.strip()) == 0 or len(endereco.strip()) == 0 or len(nicho.strip()) == 0 or len(caracteristicas.strip()) == 0 or (not logo)): 
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/home/nova_empresa')

        if logo.size > 100_000_000:
            messages.add_message(request, constants.ERROR, 'Sua logo não pode ser maior ou menor do que 10MB')
            return redirect('/home/nova_empresa')

        if nicho not in [i[0] for i in Empresa.choices_nicho_mercado]:
            messages.add_message(request, constants.ERROR, 'Nicho de mercado inválido')
            return redirect('/home/nova_empresa')
        
        empresa = Empresa(logo=logo,
                        nome=nome,
                        email=email,
                        cidade=cidade,
                        endereco=endereco,
                        nicho_mercado=nicho,
                        caracteristica_empresa=caracteristicas)
        empresa.save()
        empresa.tecnologias.add(*tecnologias)
        empresa.save()
        messages.add_message(request, constants.SUCCESS, 'Empresa cadastrada com sucesso')
        return redirect('/home/empresas')
    
def empresas(request):
    filtrar_tecnologias = request.GET.get('tecnologias')
    filtrar_nome = request.GET.get('nome')
    empresas = Empresa.objects.all()
    
    if filtrar_tecnologias:
        empresas = empresas.filter(tecnologias=filtrar_tecnologias)
        
    if filtrar_nome:
        empresas = empresas.filter(nome__icontains=filtrar_nome)
    
    tecnologias = Tecnologias.objects.all()
    return render(request, 'empresa.html', {'empresas': empresas, 'tecnologias': tecnologias})

def excluir_empresa(request, id):
    empresa = Empresa.objects.get(id=id)
    empresa.delete()
    messages.add_message(request, constants.SUCCESS, 'Empresa excluída com sucesso')
    return redirect('/home/empresas')
    
def empresa(request, id):
    empresa_unica = get_object_or_404(Empresa, id=id)
    return render(request, 'empresa_unica.html', {'empresa': empresa_unica})



    