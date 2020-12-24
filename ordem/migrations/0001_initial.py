# Generated by Django 3.1.4 on 2020-12-24 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ativo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ordem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_compra', models.DecimalField(decimal_places=2, max_digits=20)),
                ('data_compra', models.CharField(max_length=40)),
                ('valor_venda', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True)),
                ('data_venda', models.CharField(blank=True, max_length=40, null=True)),
                ('lucro', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('esta_ativa', models.BooleanField()),
                ('ativo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ativo.ativo')),
            ],
        ),
    ]
