# Generated by Django 3.2.8 on 2022-01-14 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0012_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='notes',
            field=models.TimeField(max_length=500, null=True),
        ),
    ]