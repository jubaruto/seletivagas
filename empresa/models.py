from django.db import models

class Tecnologias(models.Model):
    tecnologia = models.CharField(max_length=30)
    
    def __str__(self):
        return self.tecnologia

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
        ('DS', 'Desenvolvedor de Software'),
        ('MT', 'Motorista'),
        ('AS', 'Assitente Social'),
        ('FM', 'Farmácia'),
        ('PR', 'Professor')
    )
    logo = models.ImageField(upload_to="logo_empresa", null=True)
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    cidade = models.CharField(max_length=30)
    endereço = models.CharField(max_length=30)
    tecnologias = models.ManyToManyField(Tecnologias)
    carac_empresa = models.TextField()
    nicho_mercado = models.CharField(max_length=5, choices=choices_nicho_mercado)
    
    def __str__(self):
        return self.nome

class Vagas(models.Model):
    choices_experiencia = (
        ('J', 'Júnior'),
        ('P', 'Pleno'),
        ('S', 'Sênior')
    )

    choices_status = (
        ('I', 'Interesse'),
        ('C', 'Currículo enviado'),
        ('E', 'Entrevista'),
        ('D', 'Desafio técnico'),
        ('F', 'Finalizado')
    )
    
    empresa = models.ForeignKey(Empresa, null=True, on_delete=models.SET_NULL)
    titulo = models.CharField(max_length=30)
    nivel_experiencia = models.CharField(max_length=2, choices=choices_experiencia)
    data_final = models.DateField()
    status = models.CharField(max_length=30, choices=choices_status)
    tecnologias_dominadas = models.ManyToManyField(Tecnologias)
    tecnologias_estudar = models.ManyToManyField(Tecnologias, related_name='estudar')


    def __str__(self):
        return self.titulo
    
