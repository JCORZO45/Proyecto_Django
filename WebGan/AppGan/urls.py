from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('noticias/', views.noticias, name='noticias'),
    path('foro/', views.foro, name='foro'),
    path('compra-venta/', views.compra_venta, name='compra_venta'),
    path('mi-ganado/', views.mi_ganado, name='mi_ganado'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),  # Redirige al inicio después del logout
    path('registro/', views.registro_view, name='registro'),
    path('acerca-de-nosotros/', views.acerca_de_nosotros, name='acerca_de_nosotros'),
    path('perfil/', views.perfil_view, name='perfil'),
]