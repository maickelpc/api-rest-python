# Generated by Django 2.1.5 on 2019-03-30 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acelerometro', '0003_leitura_registro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leitura',
            name='acelerometro',
        ),
        migrations.AddField(
            model_name='arquivo',
            name='acelerometro',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='acelerometro', to='acelerometro.Acelerometro'),
            preserve_default=False,
        ),
    ]
