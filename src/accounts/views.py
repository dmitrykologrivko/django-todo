from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from tasks.models import Task


# Create your views here.
class RegistrationFormView(FormView):
    form_class = UserCreationForm
    success_url = '/accounts/login'
    template_name = 'register.html'

    def assign_default_permissions(self, form):
        # Get user
        username = form.cleaned_data['username']
        user = User.objects.get(username=username)
        # Get permissions
        content_type = ContentType.objects.get_for_model(Task)
        permViewTask = Permission.objects.get(content_type=content_type, codename='view_task')
        permAddTask = Permission.objects.get(content_type=content_type, codename='add_task')
        permChangeTask = Permission.objects.get(content_type=content_type, codename='change_task')
        permDeleteTask = Permission.objects.get(content_type=content_type, codename='delete_task')
        # Add permissions for an user
        user.user_permissions.add(permViewTask)
        user.user_permissions.add(permAddTask)
        user.user_permissions.add(permChangeTask)
        user.user_permissions.add(permDeleteTask)

    def form_valid(self, form):
        form.save()
        self.assign_default_permissions(form)
        return super().form_valid(form)
