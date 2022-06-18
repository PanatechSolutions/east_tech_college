# Generated by Django 4.0.3 on 2022-05-01 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0010_rename_duration_customize_home_page_gallery_courses_course_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customize_study_with_section',
            name='carousel_button',
        ),
        migrations.RemoveField(
            model_name='customize_study_with_section',
            name='carousel_second_message',
        ),
        migrations.AddField(
            model_name='customize_study_with_section',
            name='major_reason',
            field=models.TextField(default='Quality Knowledge', max_length=200),
        ),
        migrations.AddField(
            model_name='customize_study_with_section',
            name='minor_details',
            field=models.TextField(default='Learn from the best Instructors', max_length=500),
        ),
        migrations.AddField(
            model_name='customize_study_with_section',
            name='picture_label',
            field=models.TextField(default='As a East Technical College, we boasts of a number of reasons to why join us.', max_length=200),
        ),
        migrations.AddField(
            model_name='customize_study_with_section',
            name='reason_pics',
            field=models.ImageField(default='easttech logo.jfif', upload_to='Reason Gallery'),
        ),
    ]