from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from calendario.forms import AtividadesForm
from calendario.models import atividades
from django.core.paginator import Paginator
import calendar
from datetime import datetime, date
from django.contrib.auth import logout

def exit(request):
    logout(request)
    return redirect('home')

@login_required
def home(request):
    return render(request, 'index.html')

@login_required
def calendario(request):
    mes = int(request.GET.get('month', date.today().month))
    ano = int(request.GET.get('year', date.today().year))
    cal = calendar.monthcalendar(ano, mes)
    eventos = atividades.objects.filter(data__year=ano, data__month=mes)
    context = { 'cal': cal,
                'mes_atual': calendar.month_name[mes],
                'ano_atual': ano,
                'eventos': eventos,
                'anterior_mes': mes - 1 if mes > 1 else 12,
                'proximo_mes': mes + 1 if mes < 12 else 1,
                'ano': ano,  }
    return render(request, 'calendario.html', context)


@login_required
def listar(request):
    data = {}
    search = request.GET.get('search')

    if search:
        data['db'] = atividades.objects.filter(titulo__icontains=search).order_by('data')
    else:
        data['db'] = atividades.objects.all().order_by('data')

    all = data['db']

    paginator = Paginator(all, 4)
    pages = request.GET.get('page')

    data['db'] = paginator.get_page(pages)
    return render(request, 'listar.html', data)

@login_required
def adicionar(request):
    data = {}
    data['form'] = AtividadesForm()
    return render(request, 'adicionar.html', data)

@login_required
def create(request):
    if request.method == 'POST':
        form = AtividadesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adicionar')  # Redirecionar para a página inicial após salvar o evento
        else:
            form = AtividadesForm()
    print(form)
    return render(request, 'adicionar.html', {'form': form})

@login_required
def detalhes(request, pk):
    data = {}
    data['db'] = atividades.objects.get(pk=pk)
    return render(request, 'detalhes.html', data)

@login_required
def edit(request, pk):
    data = {}
    data['db'] = atividades.objects.get(pk=pk)
    data['form'] = AtividadesForm(instance=data['db'])
    return render(request, 'adicionar.html', data)

@login_required
def update(request, pk):
    data = {}
    data['db'] = atividades.objects.get(pk=pk)
    form = AtividadesForm(request.POST or None, instance=data['db'])
    if form.is_valid():
       form.save()
    return redirect('listar')

@login_required
def delete(request, pk):
    db = atividades.objects.get(pk=pk)
    db.delete()
    return redirect('listar')

