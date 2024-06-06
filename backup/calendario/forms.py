from django.forms import ModelForm
from calendario.models import atividades
from django import forms

class AtividadesForm(ModelForm):
    titulo = forms.CharField(widget=forms.Textarea(attrs={'rows': 1, 'cols': 100}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))

    class Meta:
        model  = atividades
        fields = ["titulo", "descricao", "area", "data", "hora"]
        labels = {
            'titulo': 'Título do Evento',
            'descricao': 'Descrição do Evento',
            'area': 'Squad',
            'data': 'Data do Evento',
            'hora': 'Hora do Evento',
        }
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
        }




