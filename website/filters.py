from helloworld.models import Estudante
import django_filters


class UserFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')
    celular = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Estudante
        fields = ['nome', 'celular', 'email']
