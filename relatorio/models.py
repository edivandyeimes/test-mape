# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Consulta(models.Model):
    numero_guia = models.IntegerField(primary_key=True)
    cod_medico = models.IntegerField()
    nome_medico = models.CharField(max_length=100, blank=True, null=True)
    data_consulta = models.DateField(blank=True, null=True)
    valor_consulta = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consulta'


class Exame(models.Model):
    numero_guia_consulta = models.ForeignKey(Consulta, models.DO_NOTHING, db_column='numero_guia_consulta')
    exame = models.CharField(primary_key=True, max_length=100)
    valor_exame = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exame'
        unique_together = (('exame', 'numero_guia_consulta'),)
