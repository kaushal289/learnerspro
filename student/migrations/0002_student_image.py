# Generated by Django 4.0 on 2022-06-06 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.FileField(blank=True, upload_to='image'),
        ),
    ]
