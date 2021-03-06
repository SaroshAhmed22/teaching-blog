# Generated by Django 3.2 on 2021-08-27 10:06

import casting.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=500)),
                ('profile_pic', models.ImageField(blank=True, upload_to=casting.models.path_and_rename, verbose_name='Profile Picture')),
                ('cell', models.IntegerField(max_length=15)),
                ('email', models.EmailField(max_length=50)),
                ('teacher_type', models.CharField(choices=[('Engineering', 'teacher'), ('None_Engineering', 'student')], default='Engineering', max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=500)),
                ('profile_pic', models.ImageField(blank=True, upload_to=casting.models.path_and_rename, verbose_name='Profile Picture')),
                ('cell', models.IntegerField(max_length=15)),
                ('email', models.EmailField(max_length=50)),
                ('student_type', models.CharField(choices=[('student', 'student'), ('cr', 'cr'), ('acr', 'acr')], default='student', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('capacity', models.IntegerField(default=40, max_length=15)),
                ('acr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='rnacr', to='casting.student')),
                ('advisor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='rntr', to='casting.teacher')),
                ('cr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='rncr', to='casting.student')),
            ],
        ),
    ]
