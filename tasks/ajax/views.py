from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render_to_response

from guardian.mixins import PermissionRequiredMixin
from guardian.shortcuts import assign_perm

from todo.mixins import (
    AjaxCreateMixin,
    AjaxUpdateMixin,
    AjaxDeleteMixin
)
from ..models import Task


class TaskCreateAjaxView(PermissionRequiredMixin, AjaxCreateMixin, CreateView):
    template_name = 'task_item.html'
    context_object_name = 'task'
    model = Task
    fields = ['description']
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


class TaskUpdateAjaxView(PermissionRequiredMixin, AjaxUpdateMixin, UpdateView):
    template_name = 'task_item.html'
    context_object_name = 'task'
    model = Task
    fields = ['description', 'is_done']
    permission_required = ['tasks.view_task', 'tasks.change_task']
    raise_exception = True


class TaskDoneAjaxView(PermissionRequiredMixin, AjaxUpdateMixin, UpdateView):
    template_name = 'task_item.html'
    context_object_name = 'task'
    model = Task
    fields = ['is_done']
    permission_required = ['tasks.view_task', 'tasks.change_task']
    raise_exception = True


class TaskDeleteAjaxView(PermissionRequiredMixin, AjaxDeleteMixin, DeleteView):
    model = Task
    permission_required = ['tasks.view_task', 'tasks.delete_task']
    raise_exception = True
