from django.db import models

# Create your models here.

class Perspectiva(models.Model):
    descricao =models.CharField(max_length=25 , blank = False , null = False)
    class Meta:
       verbose_name_plural = 'Perspectivas'
    def __str__(self):
       return self.descricao

class ObjetivoEstrategico(models.Model):
    descricao =models.CharField(max_length=200 , blank = False , null = False)
    perspectiva = models.ForeignKey(Perspectiva , related_name = 'perspectivas' , on_delete = models.CASCADE)
    class Meta:
       verbose_name_plural = 'Objetivos Estratégicos'
    def __str__(self):
       return self.descricao + '-' + self.perspectiva

class AcoesOrcamentarias(models.Model):
    descricao =models.CharField(max_length=200 , blank = False , null = False)
    objetivoestrategico =models.ForeignKey(ObjetivoEstrategico , related_name = 'objetivos_estratégicos' , on_delete = models.CASCADE)
    responsavel =models.CharField(max_length=50 , blank = False , null = False)
    prioridade = models.IntegerField()
    class Meta:
        verbose_name_plural = 'Ações Orçamentárias'
    def __str__(self):
        return self.descricao

class NaturezadeDespesa(models.Model):
    rubrica = models.IntegerField()
    descricao = models.CharField(max_length = 200 , blank = False , null = False)
    class Meta:
        verbose_name_plural = 'Natureza de Despesas'
    def __str__(self):
        return self.rubrica

class AquisicoesOrcamentarias(models.Model):
    acaoorcamentaria
    descricaodaaquisicao
    tipo
    
    
