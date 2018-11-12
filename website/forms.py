from helloworld.models import Estudante, CursoPeriodoEstudante
from django import forms

# FORMULÁRIO DE INCLUSÃO DE ESTUDANTES
# -------------------------------------------


class InsereEstudanteForm(forms.ModelForm):

    class Meta:
        # Modelo base
        model = Estudante

        # Campos que estarão no form
        fields = [
            'nome',
            'matricula',
            'email',
            'endereco',
            'cpf',
            'celular',
            'diaAniversario',
            'mesAniversario',
            'batismo',
            'escolaridade',
            'profissao'
        ]


class MatriculaMembroForm(forms.ModelForm):

    class Meta:
        # Modelo base
        model = CursoPeriodoEstudante

        # Campos que estarão no form
        fields = [
            'estudante',
            'cursoPeriodo'

        ]

class AtualizaPagamentoForm(forms.ModelForm):

    class Meta:
        # Modelo base
        model = CursoPeriodoEstudante

        # Campos que estarão no form
        fields = [
            'estudante',
            'pagamento'

        ]
