# Generated by Django 4.2.4 on 2023-08-15 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papasburgueria', '0005_hamburguer_avaliacao_remove_hamburguer_ingredientes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hamburguer',
            name='ingredientes',
            field=models.ManyToManyField(related_name='hamburguer', to='papasburgueria.ingrediente'),
        ),
    ]
