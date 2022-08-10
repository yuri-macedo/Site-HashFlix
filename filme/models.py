from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

LISTA_CATEGORIAS=(
    ("ANALISE","Análise"),
    ("PROGRAMACAO", "Programação"),
    ("APRESENTACAO", "Apresentação"),
    ("OUTROS", "Outros")
)

# Create your models here.

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=2000)
    categoria = models.CharField(choices=LISTA_CATEGORIAS,max_length=30)
    thumb = models.ImageField(upload_to="thumb_filmes")
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.titulo

class Episodio(models.Model):
    filme = models.ForeignKey("Filme",related_name="episodio",on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()
    def __str__(self):
        return self.filme.titulo + " - " + self.titulo

class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField("Filme")
