from django.db import models

# Create your models here.
CHOICES_AQUISICOES_STATUS = (
 (False , "Capital"),
 (True , "Custeio")
 )

CHOICES_PGC_STATUS = (
(False, "Não"),
(True, "Sim")
 )


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
    descricao =models.TextField(max_length=200 , blank = False , null = False)
    objetivoestrategico =models.ForeignKey(ObjetivoEstrategico , related_name = 'objetivos_estratégicos' , on_delete = models.CASCADE)
    responsavel =models.CharField(max_length=50 , blank = False , null = False)
    prioridade = models.IntegerField()
    class Meta:
        verbose_name_plural = 'Ações Orçamentárias'
    def __str__(self):
        return self.descricao

class NaturezadeDespesa(models.Model):
    rubrica = models.IntegerField()
    descricao = models.TextField(max_length = 200 , blank = False , null = False)
    class Meta:
        verbose_name_plural = 'Natureza de Despesas'
    def __str__(self):
        return self.rubrica

class AquisicoesOrcamentarias(models.Model):
    acaoorcamentaria =models.ForeignKey(AcoesOrcamentarias , related_name= 'acoes_orcamentarias' ,  on_delete = models.CASCADE)
    descricaodaaquisicao =models.TextField(max_length=200 , blank=False , null=False)
    tipo =models.BooleanField("Tipo:" , choices = CHOICES_AQUISICOES_STATUS)
    naturezadedespesa =models.ForeignKey(NaturezadeDespesa , related_name='natureza_de_despesa' , on_delete = models.CASCADE)
    quantidade = models.IntegerField()
    valorunitario = models.DecimalField(decimal_places=2 , max_digits=6)
    pgc = models.BooleanField("PGC:" , choices =CHOICES_PGC_STATUS)
    class Meta:
        verbose_name_plural = 'Aquisições Orçamentárias'
    def __str__(self):
        return self.descricaodaaquisicao

