# Generated by Django 3.2.9 on 2022-06-12 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0002_auto_20220613_0215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='csgostats',
            name='name',
        ),
    ]
