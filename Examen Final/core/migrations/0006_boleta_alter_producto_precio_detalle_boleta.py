# Generated by Django 5.0.6 on 2024-06-23 21:11

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_producto_idproducto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id_boleta', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.BigIntegerField()),
                ('fechaCompra', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(blank=True, null=True, verbose_name='Precio'),
        ),
        migrations.CreateModel(
            name='detalle_boleta',
            fields=[
                ('id_detalle_boleta', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('subtotal', models.BigIntegerField()),
                ('id_boleta', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='core.boleta')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto')),
            ],
        ),
    ]
