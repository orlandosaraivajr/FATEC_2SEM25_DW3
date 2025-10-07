from django import forms
from django.core.exceptions import ValidationError

class FeriadoForm(forms.Form):
    nome = forms.CharField(max_length=50)
    dia = forms.IntegerField()
    mes = forms.IntegerField()
    
    def clean_nome(self):
        nome = self.cleaned_data['nome']
        return nome.upper()
    
    def clean_dia(self):
        dia = self.cleaned_data.get('dia')
        if dia <= 0 or dia > 31:
            raise ValidationError('Dia Inválido')
    
    def clean(self):
        pass


from core.models import FeriadoModel
from django.forms import ModelForm

class FeriadoFormModel(ModelForm):
    class Meta:
        model = FeriadoModel
        fields = ['nome','dia','mes']
    
    def clean_nome(self):
        nome = self.cleaned_data['nome']
        return nome.upper()