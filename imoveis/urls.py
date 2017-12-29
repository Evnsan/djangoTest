from django.urls import path 

from . import views
app_name = 'imoveis'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:build_id>/', views.detail, name='detail'),
    path('<int:build_id>/picture', views.picture, name='picture'),
]
