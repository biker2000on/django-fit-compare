# Generated by Django 3.0.3 on 2020-05-16 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0005_auto_20200516_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='start_position_lat',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='start_position_long',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='position_lat',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='position_long',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
