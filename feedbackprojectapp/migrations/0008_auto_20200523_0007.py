# Generated by Django 3.0.3 on 2020-05-22 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedbackprojectapp', '0007_remove_facultydatabase_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facultydatabase',
            name='subject',
        ),
        migrations.AddField(
            model_name='facultydatabase',
            name='subject',
            field=models.ManyToManyField(null=True, to='feedbackprojectapp.SubjectDatabase'),
        ),
    ]