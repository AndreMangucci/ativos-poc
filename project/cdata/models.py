from django.db import models

import uuid

from project.carbon import models as cbm

# Create your models here.


class Org(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)


class Ativos(models.Model):
    oid = models.CharField(max_length=255)
    org = models.ForeignKey(Org, on_delete=models.PROTECT)
    modelo_carbon = models.ForeignKey(
        cbm.Modelo_Carbon, null=True, on_delete=models.PROTECT
    )
    has_engine = models.BooleanField()
    can_tow = models.BooleanField()
    can_be_towed = models.BooleanField()
    fg_operate = models.BooleanField(default=False)
    fg_product_transport = models.BooleanField(default=False)
    engine_power = models.FloatField(default=0)
    working_speed = models.FloatField(default=0)
    working_width = models.FloatField(default=0)
    hor_init = models.FloatField(default=0)
    km_init = models.FloatField(default=0)
    hor_current = models.FloatField(default=0)
    km_current = models.FloatField(default=0)
    avg_fuel_consumption = models.FloatField(default=0)
