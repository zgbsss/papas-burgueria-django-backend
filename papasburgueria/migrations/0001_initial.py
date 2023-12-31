# Generated by Django 4.2.5 on 2023-09-19 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bebida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.CharField(blank=True, max_length=255, null=True)),
                ('preco', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comanda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Comanda'), (2, 'Realizado'), (3, 'Pago')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Hamburguer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('preco', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, null=True)),
                ('avaliacao', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.CharField(blank=True, max_length=255, null=True)),
                ('preco', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lucro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, null=True)),
                ('semana', models.CharField(max_length=255)),
                ('mes', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ItensComanda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(default=1)),
                ('bebida', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='papasburgueria.bebida')),
                ('comanda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='papasburgueria.comanda')),
                ('hamburguer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='papasburgueria.hamburguer')),
                ('ingrediente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='papasburgueria.ingrediente')),
            ],
        ),
        migrations.AddField(
            model_name='hamburguer',
            name='ingredientes',
            field=models.ManyToManyField(related_name='hamburguer', to='papasburgueria.ingrediente'),
        ),
    ]
