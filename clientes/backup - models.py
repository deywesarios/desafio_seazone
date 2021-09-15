<<<<<<< HEAD
from django.db import models


class Cliente(models.Model):
    GENERO_CHOICES = (
        ('1', u'Masculino'),
        ('0', u'Feminino'),
        ('2', u'Não Informar'),
    )

    nome = models.CharField(max_length=60, verbose_name="Nome do Hóspede",
                            help_text="Coloque aqui o nome do hóspede a ser registrado.")
    cpf = models.CharField(max_length=11, blank=True, null=True)
    dtNascimento = models.DateField(blank=True, null=True, verbose_name="Data de nascimento")
    genero = models.IntegerField(choices=GENERO_CHOICES)
    email = models.EmailField(unique=True, verbose_name='E-mail')
    celular = models.CharField(max_length=16, blank=True, null=True, verbose_name="Nº telefone celular")

    def __str__(self):
        return self.nome

# class Categoria(models.Model):
#    pass
#    nome = models.CharField(max_length=100)
#
#    def __str__(self):
#        return self.nome
#
#
# class Produto(models.Model):
#    nome = models.CharField(max_length=100, verbose_name="Nome do Produto",
#                            help_text="Coloque aqui o nome do produto a ser registrado.")
#    cpf = models.CharField(max_length=11)
#    codigo_de_barras = models.IntegerField()
#    categoria = models.ForeignKey(Categorias, related_name="produtos", on_delete=models.CASCADE)
#
#    def __str__(self):
#        return self.nome + ' - ' + self.cpf
#    class Meta:
#        verbose_name = "Produto - Preço"
#        verbose_name_plural = "Produtos e Preços"
=======
from django.db import models


class Cliente(models.Model):
    GENERO_CHOICES = (
        ('1', u'Masculino'),
        ('0', u'Feminino'),
        ('2', u'Não Informar'),
    )

    nome = models.CharField(max_length=60, verbose_name="Nome do Hóspede",
                            help_text="Coloque aqui o nome do hóspede a ser registrado.")
    cpf = models.CharField(max_length=11, blank=True, null=True)
    dtNascimento = models.DateField(blank=True, null=True, verbose_name="Data de nascimento")
    genero = models.IntegerField(choices=GENERO_CHOICES)
    email = models.EmailField(unique=True, verbose_name='E-mail')
    celular = models.CharField(max_length=16, blank=True, null=True, verbose_name="Nº telefone celular")

    def __str__(self):
        return self.nome

# class Categoria(models.Model):
#    pass
#    nome = models.CharField(max_length=100)
#
#    def __str__(self):
#        return self.nome
#
#
# class Produto(models.Model):
#    nome = models.CharField(max_length=100, verbose_name="Nome do Produto",
#                            help_text="Coloque aqui o nome do produto a ser registrado.")
#    cpf = models.CharField(max_length=11)
#    codigo_de_barras = models.IntegerField()
#    categoria = models.ForeignKey(Categorias, related_name="produtos", on_delete=models.CASCADE)
#
#    def __str__(self):
#        return self.nome + ' - ' + self.cpf
#    class Meta:
#        verbose_name = "Produto - Preço"
#        verbose_name_plural = "Produtos e Preços"
>>>>>>> 7ecf0588ac716eb8e28267220c531014cd74540b
