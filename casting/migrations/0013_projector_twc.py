# Generated by Django 3.2 on 2021-12-15 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casting', '0012_alter_room_twc'),
    ]

    operations = [
        migrations.AddField(
            model_name='projector',
            name='twc',
            field=models.IntegerField(default=1, max_length=200, null=True),
        ),
    ]