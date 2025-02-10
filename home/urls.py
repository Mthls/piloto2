from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contato/', views.contato, name='contato'),
    path('sobre/', views.sobre, name='sobre'),
    path('ajuda/', views.ajuda, name='ajuda'),
    path('local/', views.local, name='local'),
    path('perfil/', views.perfil, name='perfil'),  # URL sem argumento opcional
    path('perfil/<str:usuario>/', views.perfil, name='perfil_com_usuario'),  # URL com argumento

]
