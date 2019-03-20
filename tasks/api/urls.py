from django.conf.urls import url

from .views import TaskViewSet

COLLECTION_ACTIONS = {
    'get': 'list',
    'post': 'create'
}

OBJECT_ACTIONS = {
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
}

urlpatterns = [
    url(r'^$', TaskViewSet.as_view(COLLECTION_ACTIONS), name='list'),
    url(r'^(?P<pk>\d+)/$', TaskViewSet.as_view(OBJECT_ACTIONS), name='detail')
]
