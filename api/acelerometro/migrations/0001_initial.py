# Generated by Django 2.1.5 on 2019-03-29 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acelerometro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=100, unique=True)),
                ('descricao', models.CharField(max_length=100)),
                ('localizacao', models.CharField(max_length=100)),
                ('qtdeEixos', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Arquivo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dataLancamento', models.DateTimeField(auto_now_add=True)),
                ('dataInicialLeitura', models.DateTimeField()),
                ('frequenciaTempo', models.DecimalField(decimal_places=10, max_digits=10)),
                ('qtdeRegistros', models.BigIntegerField()),
                ('media', models.DecimalField(decimal_places=10, max_digits=10)),
                ('desvioPadrao', models.DecimalField(decimal_places=10, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Leitura',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dataLeitura', models.DateTimeField()),
                ('eixo', models.PositiveSmallIntegerField()),
                ('valor', models.DecimalField(decimal_places=10, max_digits=10, null=True)),
                ('acelerometro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acelerometro', to='acelerometro.Acelerometro')),
                ('arquivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arquivo', to='acelerometro.Arquivo')),
            ],
        ),
    ]
