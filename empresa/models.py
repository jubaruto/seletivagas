from django.db import models

class Empresa(models.Model):
    choices_nicho_mercado = (
        ('MK', 'Marketing'),
        ('NT', 'Nutrição'),
        ('DN', 'Design'),
        ('PS', 'Psicologia'),
        ('EC', 'Engenharia Civil'),
        ('FN', 'Fonoaudiologia'),
        ('EM', 'Engenharia Mecânica'),
        ('EP', 'Engenharia de Produção'),
        ('DS', 'Desenvolvedor de Software')
        ('MT', 'Motorista'),
        ('AS', 'Assitente Social'),
        ('FM', 'Farmácia'),
        ('PR', 'Professor')
    )
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    cidade = models.CharField(max_length=30)
    endereço = models.CharField(max_length=30)
    carac_empresa = models.TextField()
    nicho_mercado = models.CharField(max_length=3, choices=choices_nicho_mercado)
    
    
