# Generated by Django 4.2.7 on 2023-12-03 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_alter_course_description_alter_subject_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.course'),
        ),
    ]