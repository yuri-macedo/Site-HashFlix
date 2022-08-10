# url - view - template

from django.urls import path, include,reverse_lazy
from .views import Homepage,Homefilmes,Detalhesfilme,Pesquisa,Editarperfil,Criarconta
from django.contrib.auth import views as auth_views

app_name="filme"

urlpatterns = [
    path('', Homepage.as_view(),name="homepage"),
    path('filmes', Homefilmes.as_view(),name="homefilmes"),
    path('filmes/<int:pk>', Detalhesfilme.as_view(),name="detalhesfilme"),
    path('pesquisa', Pesquisa.as_view(),name="pesquisa"),
    path('login', auth_views.LoginView.as_view(template_name="login.html"),name="login"),
    path('logout', auth_views.LogoutView.as_view(template_name="logout.html"),name="logout"),
    path('editarperfil/<int:pk>', Editarperfil.as_view(template_name="editarperfil.html"),name="editarperfil"),
    path('criarconta', Criarconta.as_view(),name="criarconta"),
    path('editarsenha/<int:pk>', auth_views.PasswordChangeView.as_view(template_name="editarperfil.html",success_url=reverse_lazy("filme:homefilmes")),name="editarsenha"),
]