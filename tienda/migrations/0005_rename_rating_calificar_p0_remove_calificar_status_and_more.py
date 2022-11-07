# Generated by Django 4.1 on 2022-11-06 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0004_calificar_contacto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calificar',
            old_name='rating',
            new_name='p0',
        ),
        migrations.RemoveField(
            model_name='calificar',
            name='status',
        ),
        migrations.AddField(
            model_name='calificar',
            name='p1',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='calificar',
            name='p2',
            field=models.FloatField(default=0),
        ),
    ]