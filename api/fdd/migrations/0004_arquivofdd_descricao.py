# Generated by Django 2.2.4 on 2019-08-10 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fdd', '0003_auto_20190809_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='arquivofdd',
            name='descricao',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]