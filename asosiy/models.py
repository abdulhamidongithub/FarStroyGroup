from django.db import models

class Asosiy(models.Model):
    rasm = models.FileField(upload_to='asosiy')
    matn_uz = models.CharField(max_length=500)
    matn_rus = models.CharField(max_length=500)
    matn_ingliz = models.CharField(max_length=500)
    def __str__(self):
        return self.matn_uz

class KaryuselRasm(models.Model):
    rasm = models.FileField(upload_to='karyusel')

class Katalog(models.Model):
    nom_uz = models.CharField(max_length=300)
    nom_rus = models.CharField(max_length=300)
    nom_ingliz = models.CharField(max_length=300)
    loyiha_haqida_uz = models.CharField(max_length=300)
    loyiha_haqida_rus = models.CharField(max_length=300)
    loyiha_haqida_ingliz = models.CharField(max_length=300)
    loyiha_haqida_rasm = models.FileField('loyiha_haqida')
    bizning_ishlar_uz = models.CharField(max_length=300)
    bizning_ishlar_rus = models.CharField(max_length=300)
    bizning_ishlar_ingliz = models.CharField(max_length=300)
    bizning_ishlar_rasm = models.FileField(upload_to='bizning_ishlar')
    infratuzilma_uz = models.CharField(max_length=300)
    infratuzilma_rus = models.CharField(max_length=300)
    infratuzilma_ingliz = models.CharField(max_length=300)
    infratuzilma_rasm = models.FileField(upload_to='infratuzilma')
    afzalliklar_uz = models.CharField(max_length=300)
    afzalliklar_rus = models.CharField(max_length=300)
    afzalliklar_ingliz = models.CharField(max_length=300)
    afzalliklar_rasm = models.FileField(upload_to='afzalliklar')

class Fasad(models.Model):
    rasm = models.FileField(upload_to='fasad')

class BizningUylar(models.Model):
    nom_uz = models.CharField(max_length=150)
    nom_rus = models.CharField(max_length=150)
    nom_ingliz = models.CharField(max_length=150)
    kenglik = models.PositiveSmallIntegerField()
    kirish = models.PositiveSmallIntegerField()
    mehmonxona = models.PositiveSmallIntegerField()
    oshxona = models.PositiveSmallIntegerField()
    shahar = models.CharField(max_length=150)
    sotuvda_bor = models.BooleanField(default=True)
    def __str__(self):
        return self.nom_uz
