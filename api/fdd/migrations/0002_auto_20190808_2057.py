# Generated by Django 2.2.4 on 2019-08-08 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fdd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arquivo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]