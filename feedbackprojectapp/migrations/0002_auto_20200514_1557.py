# Generated by Django 3.0.6 on 2020-05-14 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedbackprojectapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackform',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='feedbackanswers',
            name='total_rating',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='feedbackform',
            name='total_rating',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
