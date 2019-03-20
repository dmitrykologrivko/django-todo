from django_filters import FilterSet, IsoDateTimeFilter

from ..models import Task


class TaskFilter(FilterSet):
    created_from = IsoDateTimeFilter(field_name='created', lookup_expr='gte')
    created_to = IsoDateTimeFilter(field_name='created', lookup_expr='lte')
    updated_from = IsoDateTimeFilter(field_name='updated', lookup_expr='gte')
    updated_to = IsoDateTimeFilter(field_name='updated', lookup_expr='lte')

    class Meta:
        model = Task
        fields = ['is_done', 'created', 'updated']
