# Generated by Django 4.2.3 on 2023-07-19 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='full_name',
            field=models.CharField(max_length=255, verbose_name='Name of User'),
        ),
    ]