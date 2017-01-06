from django.shortcuts import render_to_response

from ajax_views import AjaxCreateView, AjaxUpdateView, AjaxDeleteView
from guardian.mixins import PermissionRequiredMixin
from guardian.shortcuts import assign_perm

from ..models import Task


class TaskCreateAjaxView(PermissionRequiredMixin, AjaxCreateView):
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

    def response(self, **kwargs):
        return render_to_response('task_item.html', {'task': self.object})


class TaskUpdateAjaxView(PermissionRequiredMixin, AjaxUpdateView):
    model = Task
    fields = ['description', 'is_done']
    permission_required = ['tasks.view_task', 'tasks.change_task']
    raise_exception = True

    def response(self, **kwargs):
        return render_to_response('task_item.html', {'task': self.object})


class TaskDoneAjaxView(PermissionRequiredMixin, AjaxUpdateView):
    model = Task
    fields = ['is_done']
    permission_required = ['tasks.view_task', 'tasks.change_task']
    raise_exception = True

    def response(self, **kwargs):
        return render_to_response('task_item.html', {'task': self.object})


class TaskDeleteAjaxView(PermissionRequiredMixin, AjaxDeleteView):
    model = Task
    permission_required = ['tasks.view_task', 'tasks.delete_task']
    raise_exception = True
