# Generated by Django 5.1.7 on 2025-03-28 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cdata", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ativos",
            name="avg_fuel_consumption",
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name="ativos",
            name="engine_power",
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name="ativos",
            name="working_speed",
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name="ativos",
            name="working_width",
            field=models.FloatField(null=True),
        ),
    ]
