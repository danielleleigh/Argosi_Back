# Generated by Django 3.2.8 on 2022-01-14 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0009_auto_20220114_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='birth_time',
            field=models.TimeField(max_length=50, null=True),
        ),
    ]