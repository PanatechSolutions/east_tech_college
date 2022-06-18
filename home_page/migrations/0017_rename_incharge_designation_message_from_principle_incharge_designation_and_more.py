# Generated by Django 4.0.3 on 2022-05-08 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0016_message_from_principle_incharge_designation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message_from_principle',
            old_name='incharge_designation',
            new_name='Incharge_designation',
        ),
        migrations.RemoveField(
            model_name='message_from_principle',
            name='designation',
        ),
        migrations.AddField(
            model_name='message_from_principle',
            name='Incharge_message',
            field=models.TextField(default='Welcome to East Technical College', max_length=600),
        ),
    ]
