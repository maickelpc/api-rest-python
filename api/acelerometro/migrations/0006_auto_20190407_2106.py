# Generated by Django 2.1.5 on 2019-04-07 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acelerometro', '0005_arquivo_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arquivo',
            name='desvioPadrao',
            field=models.DecimalField(decimal_places=10, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='arquivo',
            name='media',
            field=models.DecimalField(decimal_places=10, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='leitura',
            name='valor',
            field=models.FloatField(),
        ),
    ]
