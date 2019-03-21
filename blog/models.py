from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.nome

class Autor(models.Model):
    nome = models.CharField(max_length=60, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.nome


class Post(models.Model):
    titulo = models.CharField(max_length=200, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    conteudo = models.TextField(null=False, blank=False)
    data_publicacao = models.DateField(auto_now_add=True)
    categorias = models.ManyToManyField('Categoria')
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.titulo

