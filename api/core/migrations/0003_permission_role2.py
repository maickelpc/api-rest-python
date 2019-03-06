# Generated by Django 2.1.5 on 2019-02-10 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_permission_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='permissions',
            field=models.ManyToManyField(related_name='permissions', to='core.Permission'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='roles', to='core.Role'),
        ),
    ]
