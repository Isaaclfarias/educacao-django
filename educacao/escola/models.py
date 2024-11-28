


from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

class Curso(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo

