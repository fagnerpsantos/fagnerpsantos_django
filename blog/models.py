from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)

class Post(models.Model):
    titulo = models.CharField(max_length=200, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    conteudo = models.TextField(null=False, blank=False)
    categorias = models.ManyToManyField('Categoria')

