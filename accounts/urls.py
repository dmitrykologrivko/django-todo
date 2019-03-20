from django.conf.urls import url
from django.contrib.auth.views import login, logout

from .views import RegistrationFormView

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'logout.html'}, name='logout'),
    url(r'^register/$', RegistrationFormView.as_view(), name='register'),
]
