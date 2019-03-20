"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from oauth2_provider.views import TokenView
from rest_framework_swagger.views import get_swagger_view

from .static import static

schema_view = get_swagger_view(title='Todo API')

# general
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls'), name='accounts'),
    url(r'^', include('tasks.urls'), name='tasks'),
]

# ajax
urlpatterns += [
    url(r'^ajax/tasks/', include('tasks.ajax.urls'), name='tasks-ajax'),
]

# API
urlpatterns += [
    url(r'^api/o/token/$', TokenView.as_view(), name='oauth2-token'),
    url(r'^api/docs/$', schema_view, name='api-docs'),
    url(r'^api/tasks/', include('tasks.api.urls'), name='tasks-api'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
