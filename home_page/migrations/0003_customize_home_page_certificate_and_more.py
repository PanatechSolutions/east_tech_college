# Generated by Django 4.0.3 on 2022-05-01 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0002_customize_home_page_etc_mail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customize_home_page',
            name='certificate',
            field=models.CharField(default='8am', max_length=200),
        ),
        migrations.AddField(
            model_name='customize_home_page',
            name='closing_time',
            field=models.CharField(default='4pm', max_length=20),
        ),
        migrations.AddField(
            model_name='customize_home_page',
            name='diploma',
            field=models.CharField(default='8am', max_length=200),
        ),
        migrations.AddField(
            model_name='customize_home_page',
            name='edu_level',
            field=models.CharField(choices=[('Certificate', 'Certificate'), ('Diploma', 'Diploma'), ('Degree', 'Degree')], default='Certificate', max_length=50),
        ),
        migrations.AlterField(
            model_name='customize_home_page',
            name='ETC_mail',
            field=models.CharField(default='easttechnicalcollege@gmail.com', max_length=200),
        ),
        migrations.AlterField(
            model_name='customize_home_page',
            name='ETC_phone',
            field=models.CharField(default='0792094889', max_length=20),
        ),
        migrations.AlterField(
            model_name='customize_home_page',
            name='carousel_button',
            field=models.CharField(default='Apply', max_length=20),
        ),
        migrations.AlterField(
            model_name='customize_home_page',
            name='carousel_message',
            field=models.CharField(default='Value Added Education', max_length=200),
        ),
        migrations.AlterField(
            model_name='customize_home_page',
            name='carousel_second_message',
            field=models.CharField(default='Join us Now', max_length=200),
        ),
        migrations.AlterField(
            model_name='customize_home_page',
            name='home_carousel_pics',
            field=models.ImageField(default='8am', upload_to='Site Carousels'),
        ),
        migrations.AlterField(
            model_name='customize_home_page',
            name='office_venue',
            field=models.CharField(default='Ushirika Plaza, Chuka', max_length=150),
        ),
        migrations.AlterField(
            model_name='customize_home_page',
            name='opening_time',
            field=models.CharField(default='8am', max_length=20),
        ),
        migrations.AlterField(
            model_name='customize_home_page',
            name='school_logo',
            field=models.ImageField(default='8am', upload_to='Site Images'),
        ),
    ]