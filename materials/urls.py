from django.conf.urls import url
from . import views

app_name = 'materials'
urlpatterns = [
       url(r'^$', views.IndexView.as_view(), name='index'),
       url(r'^[-\w]+/$', views.DetailView.as_view(), name='detail'),
]