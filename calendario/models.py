from django.db import models

class Squad(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class atividades(models.Model):
    titulo    = models.CharField(max_length=80)
    descricao = models.CharField(max_length=200)
    area      = models.ForeignKey(Squad, on_delete=models.CASCADE)
    data      = models.DateField()
    hora      = models.TimeField()


