from django.db import models

import uuid

from project.carbon import models as cbm

# Create your models here.


class Org(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=255)


class Ativos(models.Model):
    org = models.ForeignKey(Org, on_delete=models.PROTECT)
    oid = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    modelo_carbon = models.ForeignKey(
        cbm.Modelo_Carbon, null=True, on_delete=models.PROTECT
    )
    has_engine = models.BooleanField()
    can_tow = models.BooleanField()
    can_be_towed = models.BooleanField()
    fg_operate = models.BooleanField(
        default=False
    )   # Pode fazer operações no talhão
    fg_product_transport = models.BooleanField(
        default=False
    )   # Pode fazer operações de transporte de produto sem consumir (nesse caso é necessário relacionar a operação)
    engine_power = models.FloatField(null=True)
    working_width = models.FloatField(null=True)
    hor_init = models.FloatField(default=0)
    km_init = models.FloatField(default=0)
    hor_current = models.FloatField(default=0)
    km_current = models.FloatField(default=0)
    avg_fuel_consumption = models.FloatField(null=True)

    class Meta:
        unique_together = (('org', 'oid'), ('org', 'name'))
