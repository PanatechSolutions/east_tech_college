# Generated by Django 4.0.3 on 2022-05-01 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0013_alter_customize_home_page_gallery_courses_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='customize_home_page_gallery_courses',
            name='course_require',
            field=models.CharField(default='KCSE Mean Grade C', max_length=200),
        ),
    ]