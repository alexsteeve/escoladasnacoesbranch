from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, DetailView
from helloworld.models import Estudante, Curso, Materia, CursoPeriodo, CursoPeriodoEstudante
from website.forms import InsereEstudanteForm, MatriculaMembroForm
from datetime import datetime
from .filters import UserFilter
from django.shortcuts import render


# PÁGINA PRINCIPAL
# ----------------------------------------------

class IndexTemplateView(TemplateView):
    template_name = "website/index.html"

# LISTA DE ESTUDANTES
# ----------------------------------------------


class EstudanteListView(ListView):
    template_name = "website/lista.html"
    model = Estudante
    context_object_name = "estudantes"
    ordering = ['nome']

# CADASTRAMENTO DE ESTUDANTES
# ----------------------------------------------

class EstudanteCreateView(CreateView):
    template_name = "website/cria.html"
    model = Estudante
    form_class = InsereEstudanteForm
    success_url = reverse_lazy("website:lista_estudantes")




# ATUALIZAÇÃO DE ESTUDANTES
# ----------------------------------------------

class EstudanteUpdateView(UpdateView):
    template_name = "website/atualiza.html"
    model = Estudante
    fields = '__all__'
    context_object_name = 'estudante'
    success_url = reverse_lazy("website:lista_estudantes")


# EXCLUSÃO DE ESTUDANTES
# ----------------------------------------------

class EstudanteDeleteView(DeleteView):
    template_name = "website/exclui.html"
    model = Estudante
    context_object_name = 'estudante'
    success_url = reverse_lazy("website:lista_estudantes")


# LISTA DE ANIVERSARIANTES
# ----------------------------------------------


class AniversariantesListView(ListView):
    this_month = datetime.now().month
    next_month = datetime.now().month + 1
    template_name = "website/aniversariantes.html"
    model = Estudante
    context_object_name = "estudantes"
    ordering = ['diaAniversario']
    queryset = Estudante.objetos.filter(mesAniversario=this_month)
    ordering_fields = ('nome' , 'email')

# PERFIL DO ESTUDANTE
# ----------------------------------------------


class EstudantePerfilView(DetailView):
    template_name = "website/estudante.html"
    model = Estudante
    context_object_name = "estudante"

    def get_context_data(self, **kwargs):
        context = super(EstudantePerfilView, self).get_context_data(**kwargs)
        context['cursoperiodoestudante'] = CursoPeriodoEstudante.objetos.filter(estudante_id=self.kwargs['pk'])
        return context


# LISTA DE CURSOS
# ----------------------------------------------


class CursoListView(ListView):
    template_name = "website/listacursos.html"
    model = Curso
    context_object_name = "cursos"

# PERFIL DO CURSO
# ----------------------------------------------


class CursoPerfilView(DetailView):
    template_name = "website/cursos.html"
    model = Curso
    context_object_name = "curso"

    def get_context_data(self, **kwargs):
        context = super(CursoPerfilView, self).get_context_data(**kwargs)
        context['materia'] = Materia.objetos.filter(curso_id=self.kwargs['pk'])
        context['cursoperiodo'] = CursoPeriodo.objetos.filter(curso_id=self.kwargs['pk'])
        return context

# DETALHE DO CURSO COM LISTA DE ALUNOS
# ----------------------------------------------


class CursoPeriodoView(DetailView):
    template_name = "website/cursoperiodo.html"
    model = CursoPeriodo
    context_object_name = "cursoperiodo"

    def get_context_data(self, **kwargs):
        context = super(CursoPeriodoView, self).get_context_data(**kwargs)
        context['cursoperiodoestudante'] = CursoPeriodoEstudante.objetos.filter(cursoPeriodo_id=self.kwargs['pk'])
        return context


# DETALHE DA PENDENCIA DO ESTUDANTE

class CursoPeriodoPendencia(DetailView):
    template_name = "website/cursoperiodopendencia.html"
    model = CursoPeriodoEstudante
    context_object_name = "cursoperiodoestudante"

# TESTE NOVA PESQUISA


def search(request):
    user_list = Estudante.objetos.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'website/user_list.html', {'filter': user_filter})


# MATRICULA DE MEMBROS
# ----------------------------------------------

class MatriculaCreateView(CreateView):
    template_name = "website/matricula.html"
    model = CursoPeriodoEstudante
    form_class = MatriculaMembroForm
    success_url = reverse_lazy("website:lista_estudantes")
