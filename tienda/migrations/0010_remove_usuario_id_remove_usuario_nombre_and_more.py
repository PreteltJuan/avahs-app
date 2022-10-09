# Generated by Django 4.0.6 on 2022-10-05 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0009_alter_producto_idproducto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='id',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='nombre',
        ),
        migrations.AddField(
            model_name='usuario',
            name='barrio',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='correo',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='direccion',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='edad',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='idUsuario',
            field=models.AutoField(default=2, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='primer_apellido',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='primer_nombre',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='segundo_apellido',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='segundo_nombre',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='sexo',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
