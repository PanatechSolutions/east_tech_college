# Generated by Django 4.0.3 on 2022-05-08 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0015_message_from_principle'),
    ]

    operations = [
        migrations.AddField(
            model_name='message_from_principle',
            name='incharge_designation',
            field=models.CharField(default='PRINCIPAL', max_length=50),
        ),
    ]