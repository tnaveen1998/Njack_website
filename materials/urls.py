from django.conf.urls import url
from . import views

app_name = 'materials'
urlpatterns = [
       url(r'^$', views.IndexView.as_view(), name='index'),
       url(r'^(?P<name>[\w]+)/$', views.DetailView, name='detail'),
       url(r'^[?]q[=](?P<name>[\w]+)/$', views.DetailView, name='detail'),
]