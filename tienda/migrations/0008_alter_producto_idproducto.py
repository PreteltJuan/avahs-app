# Generated by Django 4.0.6 on 2022-10-05 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0007_alter_producto_idproducto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='idProducto',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]