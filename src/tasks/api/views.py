from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import (
    DjangoObjectPermissionsFilter,
    DjangoFilterBackend,
    SearchFilter,
    OrderingFilter
)
from rest_framework.permissions import DjangoModelPermissions
from guardian.shortcuts import assign_perm

from ..models import Task
from .serializers import TaskSerializer
from .filters import TaskFilter
from .permissions import TasksObjectPermissions


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoObjectPermissionsFilter,
                       DjangoFilterBackend,
                       OrderingFilter,
                       SearchFilter]
    ordering_fields = ['is_done', 'created', 'updated']
    search_fields = ['description']
    filter_class = TaskFilter
    permission_classes = [DjangoModelPermissions, TasksObjectPermissions]

    def perform_create(self, serializer):
        task = serializer.save(user=self.request.user)
        assign_perm('tasks.view_task', self.request.user, task)
        assign_perm('tasks.change_task', self.request.user, task)
        assign_perm('tasks.delete_task', self.request.user, task)
