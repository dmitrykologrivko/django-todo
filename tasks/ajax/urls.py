from django.conf.urls import url

from .views import (
    TaskCreateAjaxView,
    TaskUpdateAjaxView,
    TaskDoneAjaxView,
    TaskDeleteAjaxView
)

urlpatterns = [
    url(r'^create/$', TaskCreateAjaxView.as_view(), name='create'),
    url(r'^edit/$', TaskUpdateAjaxView.as_view(), name='edit'),
    url(r'^done/$', TaskDoneAjaxView.as_view(), name='done'),
    url(r'^delete/$', TaskDeleteAjaxView.as_view(), name='delete'),
]
