# Generated by Django 4.0.3 on 2022-06-10 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programmes', '0013_alter_applicationform_county_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
