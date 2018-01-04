from django.conf.urls import url

from . import views
app_name = 'imoveis'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<build_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<build_id>[0-9]+)/picture$', views.picture, name='picture'),
    url('add_picture', views.add_picture, name='add_picture'),
]
