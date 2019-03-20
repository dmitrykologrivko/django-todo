from django.conf.urls import url

from .views import (
    TaskCreateView,
    TasksListView,
    TaskDetailView,
    TaskUpdateView,
    TaskDeleteView
)

urlpatterns = [
    url(r'^$', TasksListView.as_view(), name='list'),
    url(r'^create/$', TaskCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', TaskDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', TaskUpdateView.as_view(), name='edit'),
    url(r'^(?P<pk>\d+)/delete/$', TaskDeleteView.as_view(), name='delete'),
]
