import pytest

pytestmark = pytest.mark.django_db

#####

from project.cdata import models


def test_main():

    org = models.Org.objects.create(name='CarbonBr')

    # Fiat Strada - Veículo

    strada = models.Ativos.objects.create(
        oid='317',
        name='Fiat Strada',
        org=org,
        modelo_carbon=None,
        has_engine=True,
        can_tow=False,
        can_be_towed=False,
        fg_operate=False,
        fg_product_transport=True,
        engine_power=None,
        working_width=None,
        hor_init=0,
        km_init=156700,
        hor_current=0,
        km_current=267000,
        avg_fuel_consumption=13,
    )

    # JD 6135M - Trator

    tractor = models.Ativos.objects.create(
        oid='311',
        name='6135M',
        org=org,
        modelo_carbon=None,
        has_engine=True,
        can_tow=True,
        can_be_towed=False,
        fg_operate=False,
        fg_product_transport=False,
        engine_power=133,
        working_width=None,
        hor_init=10,
        km_init=0,
        hor_current=25,
        km_current=0,
        avg_fuel_consumption=5,
    )

    # Uniport - Implemento

    uniport = models.Ativos.objects.create(
        oid='208',
        name='Uniport 3000',
        org=org,
        modelo_carbon=None,
        has_engine=True,
        can_tow=False,
        can_be_towed=False,
        fg_operate=True,
        fg_product_transport=False,
        engine_power=237,
        working_width=32,
        hor_init=10,
        km_init=0,
        hor_current=25,
        km_current=0,
        avg_fuel_consumption=4,
    )

    # Pá carragadeira - Hibrido

    uniport = models.Ativos.objects.create(
        oid='200',
        name='CAT 996',
        org=org,
        modelo_carbon=None,
        has_engine=True,
        can_tow=False,
        can_be_towed=False,
        fg_operate=True,
        fg_product_transport=True,
        engine_power=325,
        working_width=4,
        hor_init=300,
        km_init=0,
        hor_current=400,
        km_current=0,
        avg_fuel_consumption=3,
    )
