# Generated by Django 2.1.5 on 2019-05-01 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acelerometro', '0006_auto_20190407_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arquivo',
            name='desvioPadrao',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='arquivo',
            name='media',
            field=models.FloatField(),
        ),
    ]
