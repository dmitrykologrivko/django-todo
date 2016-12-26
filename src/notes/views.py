from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Note


# Create your views here.
@method_decorator(login_required, name='dispatch')
class NoteListView(ListView):
    template_name = 'note_list.html'
    context_object_name = 'notes'

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)


@method_decorator(login_required, name='dispatch')
class NoteDetailView(DetailView):
    template_name = 'note.html'
    context_object_name = 'note'
    model = Note

    def get_object(self, queryset=None):
        note = super().get_object(queryset)
        if note.is_owner(self.request):
            return note
        else:
            raise PermissionDenied()
