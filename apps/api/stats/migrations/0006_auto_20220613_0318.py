# Generated by Django 3.2.9 on 2022-06-13 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0005_auto_20220613_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csgostats',
            name='average_hs',
            field=models.PositiveSmallIntegerField(blank=True, verbose_name='Average Headshots %'),
        ),
        migrations.AlterField(
            model_name='csgostats',
            name='win_rate',
            field=models.PositiveSmallIntegerField(blank=True, verbose_name='Win Rate %'),
        ),
    ]
