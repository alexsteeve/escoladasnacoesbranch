from website.views import IndexTemplateView,  \
     EstudanteListView, EstudanteCreateView, EstudanteUpdateView, EstudanteDeleteView, AniversariantesListView, \
     EstudantePerfilView, CursoListView, CursoPerfilView, CursoPeriodoView, CursoPeriodoPendencia, search, \
     MatriculaCreateView, PagamentoUpdateView, MatriculaDeleteView, ConfirmaPagamentoView, IndexTemplateView2,\
     search2, EstudantePerfilView2, EstudanteUpdateView2, MatriculaCreateView2, EstudanteCreateView2, \
     PagamentoUpdateView2, ConfirmaPagamentoView2
from django.conf.urls import url

from django.urls import path

app_name = 'website'

urlpatterns = [
    # GET /
    path('', IndexTemplateView.as_view(), name="index"),


    # GET /estudante/cadastrar
    path('estudante/cadastrar/', EstudanteCreateView.as_view(), name="cadastra_estudante"),

    # GET /matricula de membro/cadastrar
    path('estudante/matricular/<pk>', MatriculaCreateView.as_view(), name="matricula_membro"),

    # GET /estudantes
    path('estudantes/', EstudanteListView.as_view(), name="lista_estudantes"),

    # GET /estudantes
    path('aniversariantes/', AniversariantesListView.as_view(), name="lista_aniversariantes"),

    # GET/POST /estudante/{pk}
    path('estudante/<pk>', EstudanteUpdateView.as_view(), name="atualiza_estudante"),

    # GET/POST /estudantes/excluir/{pk}
    path('estudante/excluir/<pk>', EstudanteDeleteView.as_view(), name="deleta_estudante"),

    # GET /estudantes/perfil/{pk}
    path('estudante/perfil/<pk>', EstudantePerfilView.as_view(), name="perfil_estudante"),

    # GET /cursos
    path('cursos/', CursoListView.as_view(), name="lista_cursos"),

    # GET /cursos/perfil/{pk}
    path('curso/perfil/<pk>', CursoPerfilView.as_view(), name="perfil_curso"),

    # GET /cursos/periodo/perfil/{pk}
    path('curso/periodo/perfil/<pk>', CursoPeriodoView.as_view(), name="periodo_curso"),

    # GET /cursos/periodo/perfil/{pk}
    path('curso/periodo/pendencia/<pk>', CursoPeriodoPendencia.as_view(), name="curso_periodo_pendencia"),

    # GET /pesquisar/
    url(r'^search/$', search, name="search"),

    # GET/POST /pagamentos/{pk}
    path('estudante/pagamento/<pk>', PagamentoUpdateView.as_view(), name="pagamento"),

    # GET/POST /estudantes/matricula/excluir/{pk}
    path('estudante/matricula/excluir/<pk>', MatriculaDeleteView.as_view(), name="deleta_matricula"),

    # GET /pagamentos-sucesso/
    path('estudante/pagamento-sucesso/', ConfirmaPagamentoView.as_view(), name="pagamento-sucesso"),

    # GET /index2/
    path('novo/', IndexTemplateView2.as_view(), name="index2"),

    # GET /pesquisar2/
    url(r'^search2/$', search2, name="search2"),

    # GET /estudante2/perfil/{pk}
    path('estudante2/perfil/<pk>', EstudantePerfilView2.as_view(), name="perfil_estudante2"),

    # GET/POST /estudante2/{pk}
    path('estudante2/<pk>', EstudanteUpdateView2.as_view(), name="atualiza_estudante2"),

    # GET /matricula de membro/cadastrar
    path('estudante/matricular2/<pk>', MatriculaCreateView2.as_view(), name="matricula_membro2"),

    # GET /estudante/cadastrar
    path('estudante/cadastrar2/', EstudanteCreateView2.as_view(), name="cadastra_estudante2"),

    # GET/POST /pagamentos/{pk}
    path('estudante/pagamento2/<pk>', PagamentoUpdateView2.as_view(), name="pagamento2"),

    # GET /pagamentos-sucesso/
    path('estudante/pagamento-sucesso2/', ConfirmaPagamentoView2.as_view(), name="pagamento-sucesso2"),
]
