# Generated by Django 4.2.4 on 2023-11-30 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socios_app', '0002_alter_socio_correo_electronico'),
    ]

    operations = [
        migrations.AddField(
            model_name='socio',
            name='observacion',
            field=models.CharField(default='o', max_length=250),
            preserve_default=False,
        ),
    ]
