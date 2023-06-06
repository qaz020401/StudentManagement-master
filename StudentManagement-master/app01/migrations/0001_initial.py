# Generated by Django 4.2 on 2023-05-08 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('stu_id', models.CharField(max_length=32, unique=True)),
                ('class_id', models.CharField(max_length=32)),
                ('chinese', models.IntegerField(null=True)),
                ('math', models.IntegerField(null=True)),
                ('english', models.IntegerField(null=True)),
            ],
        ),
    ]