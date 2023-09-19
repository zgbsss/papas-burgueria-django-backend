# Generated by Django 4.2.5 on 2023-09-19 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papasburgueria', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itenscomanda',
            name='bebida',
        ),
        migrations.RemoveField(
            model_name='itenscomanda',
            name='hamburguer',
        ),
        migrations.RemoveField(
            model_name='itenscomanda',
            name='ingrediente',
        ),
        migrations.AddField(
            model_name='itenscomanda',
            name='bebida',
            field=models.ManyToManyField(related_name='+', to='papasburgueria.bebida'),
        ),
        migrations.AddField(
            model_name='itenscomanda',
            name='hamburguer',
            field=models.ManyToManyField(related_name='+', to='papasburgueria.hamburguer'),
        ),
        migrations.AddField(
            model_name='itenscomanda',
            name='ingrediente',
            field=models.ManyToManyField(related_name='+', to='papasburgueria.ingrediente'),
        ),
    ]
