from django.conf.urls import url
from .views import NoteListView, NoteDetailView

urlpatterns = [
    url(r'^$', NoteListView.as_view(), name='list'),
    url(r'^(?P<pk>[\w-]+)/$', NoteDetailView.as_view(), name='detail'),
]