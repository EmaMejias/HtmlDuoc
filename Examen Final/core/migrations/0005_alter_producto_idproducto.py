# Generated by Django 5.0.6 on 2024-06-22 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_producto_descripcionproducto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='idProducto',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='id de producto'),
        ),
    ]