from django.db import models

class Cadastro(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()
    confirmar_email = models.EmailField()
    cpf_cnpj = models.CharField(max_length=20)
    cep = models.CharField(max_length=20)
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    pais = models.CharField(max_length=50)
    telefone_celular = models.CharField(max_length=20)
    telefone_comercial = models.CharField(max_length=20)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
