from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from guardian.mixins import PermissionRequiredMixin, PermissionListMixin
from guardian.shortcuts import assign_perm

from .models import Task


# Create your views here.
class TaskCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'task_create.html'
    model = Task
    fields = ['description']
    success_url = '/'
    permission_object = None
    permission_required = ['tasks.add_task']
    raise_exception = True

    def form_valid(self, form):
        form.instance.user = self.request.user
        resp = super().form_valid(form)
        assign_perm('tasks.view_task', self.request.user, self.object)
        assign_perm('tasks.change_task', self.request.user, self.object)
        assign_perm('tasks.delete_task', self.request.user, self.object)
        return resp


class TasksListView(PermissionListMixin, ListView):
    template_name = 'tasks_index.html'
    context_object_name = 'tasks'
    permission_required = ['tasks.view_task']

    def get_queryset(self):
        # Get tasks only for current user
        return Task.objects.filter(user=self.request.user)


class TaskDetailView(PermissionRequiredMixin, DetailView):
    template_name = 'task_detail.html'
    context_object_name = 'task'
    model = Task
    permission_required = ['tasks.view_task']
    raise_exception = True


class TaskUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'task_edit.html'
    model = Task
    fields = ['description', 'is_done']
    success_url = '/'
    permission_required = ['tasks.view_task', 'tasks.change_task']
    raise_exception = True


class TaskDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'task_delete.html'
    context_object_name = 'task'
    model = Task
    success_url = '/'
    permission_required = ['tasks.view_task', 'tasks.change_task']
    raise_exception = True
