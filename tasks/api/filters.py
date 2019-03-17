from django_filters import FilterSet, IsoDateTimeFilter

from ..models import Task


class TaskFilter(FilterSet):
    created_from = IsoDateTimeFilter(name='created', lookup_expr='gte')
    created_to = IsoDateTimeFilter(name='created', lookup_expr='lte')
    updated_from = IsoDateTimeFilter(name='updated', lookup_expr='gte')
    updated_to = IsoDateTimeFilter(name='updated', lookup_expr='lte')

    class Meta:
        model = Task
        fields = ['is_done', 'created', 'updated']
