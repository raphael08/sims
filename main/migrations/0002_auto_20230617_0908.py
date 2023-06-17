# Generated by Django 3.2 on 2023-06-17 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensordata',
            name='humidity_val',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='moisture_val',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='temperature_val',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='waterLevel_val',
            field=models.FloatField(default=0.0),
        ),
    ]
