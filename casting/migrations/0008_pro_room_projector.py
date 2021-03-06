# Generated by Django 3.2 on 2021-09-15 04:06

import casting.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('casting', '0007_sec_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='projector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pror_id', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, upload_to=casting.models.save_course_image, verbose_name='Subject Image')),
                ('is_active', models.BooleanField(blank=True, null=True)),
                ('capacity_run', models.IntegerField(blank=True, null=True)),
                ('t_run', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='pro_room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('proid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pro_room', to='casting.projector')),
                ('roomid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_pro', to='casting.room')),
            ],
        ),
    ]
