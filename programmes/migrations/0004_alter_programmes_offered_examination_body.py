# Generated by Django 4.0.3 on 2022-05-15 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programmes', '0003_alter_programmes_offered_examination_body_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programmes_offered',
            name='examination_body',
            field=models.CharField(choices=[('KNEC', 'KNEC'), ('KASNEB', 'KASNEB'), ('NITA', 'NITA'), ('ICDL', 'ICDL'), (models.TextField(default='Institution', max_length=200), models.TextField(default='Institution', max_length=200))], default='East Technical Institute', max_length=50),
        ),
    ]
