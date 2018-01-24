from django.conf.urls import url

from . import views
app_name = 'imoveis'
urlpatterns = [
    url(r'^$', views.BuildList.as_view(), name='index'),
    url(r'^(?P<build_id>[0-9]+)/picture$', views.picture, name='picture'),
    url(r'^(?P<pk>[0-9]+)/', views.BuildDetail.as_view(), name='detail'),
    url('add_picture', views.add_picture, name='add_picture'),
    url('add_observation', views.add_observation, name='add_observation'),
    url('add_owner', views.add_owner, name='add_owner'),
    url('add_phonenumber', views.add_phonenumber, name='add_phonenumber'),
]
