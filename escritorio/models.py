from django.db import models


class Relatorio(models.Model):
    nome = models.CharField(max_length=50)
    arquivo = models.FileField(upload_to='arquivos')

    def __str__(self) -> str:
        return f'{self.nome}'
