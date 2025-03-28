from django.db import models

# Create your models here.


class Manufactor(models.Model):
    name = models.CharField(max_length=255)


class Modelo_Carbon(models.Model):
    manufactor = models.ForeignKey(Manufactor, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    has_engine = models.BooleanField()
    can_tow = models.BooleanField(default=False)
    can_be_towed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('manufactor', 'name')
