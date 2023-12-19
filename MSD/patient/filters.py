import django_filters
from django.db.models import Q
from .models import Patient


class PatientFilter(django_filters.FilterSet):
    by_name = django_filters.CharFilter(method='filter_by_name')
    by_birthdate = django_filters.DateFilter(field_name='date_of_birth', lookup_expr='exact')
    by_type = django_filters.CharFilter(field_name='gender', lookup_expr='exact')
    by_creator = django_filters.CharFilter(method='filter_by_creator')
    by_doctor = django_filters.CharFilter(method='filter_by_doctor')
    by_nurse = django_filters.CharFilter(method='filter_by_nurse')

    class Meta:
        model = Patient
        fields = ['by_name', 'by_type', 'by_birthdate', 'by_doctor', 'by_nurse', 'by_creator']

    def filter_by_name(self, queryset, name, value):
        names = value.split(' ')
        if len(names) == 1:
            return queryset.filter(Q(first_name__icontains=names[0]) | Q(last_name__icontains=names[0]))
        else:
            return queryset.filter(Q(first_name__icontains=names[0]) & Q(last_name__icontains=names[1]))

    def filter_by_doctor(self, queryset, name, value):
        return queryset.filter(doctors__id__exact=value)

    def filter_by_nurse(self, queryset, name, value):
        return queryset.filter(nurses__id__exact=value)

    def filter_by_creator(self, queryset, name, value):
        return queryset.filter(created_by__name__exact=value)
