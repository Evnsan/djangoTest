from django.conf.urls import url

from . import views
app_name = 'imoveis'
urlpatterns = [
    url('', views.index, name='index'),
    url('<int:build_id>/', views.detail, name='detail'),
    url('<int:build_id>/picture', views.picture, name='picture'),
    url('add_picture', views.add_picture, name='add_picture'),
]
