# Generated by Django 2.0.3 on 2018-04-24 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_number',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.CharField(max_length=8, null=True),
        ),
    ]