# Generated by Django 3.2 on 2021-12-16 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casting', '0013_projector_twc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projector',
            name='t_run',
            field=models.FloatField(max_length=40),
        ),
    ]