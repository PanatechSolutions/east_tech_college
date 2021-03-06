# Generated by Django 4.0.3 on 2022-05-08 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0019_alter_message_from_principle_message_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message_From_Alumni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Alumni_designation', models.CharField(default='Business Manager', max_length=50)),
                ('Alumni_pic', models.ImageField(default='easttech logo.jfif', upload_to='Alumini')),
                ('Alumni_name', models.CharField(default='Ananymous', max_length=50)),
                ('Alumni_message', models.TextField(default='East Technical College is the place to be', max_length=600)),
            ],
        ),
    ]
