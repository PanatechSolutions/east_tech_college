# Generated by Django 4.0.3 on 2022-05-15 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programmes', '0007_programmes_offered_programme_requirements_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='programmes_offered',
            name='vacancy',
            field=models.BooleanField(default=False),
        ),
    ]
