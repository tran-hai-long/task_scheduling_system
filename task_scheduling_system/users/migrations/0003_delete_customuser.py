# Generated by Django 4.2.3 on 2023-08-07 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_full_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
