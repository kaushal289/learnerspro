# Generated by Django 4.0 on 2022-06-06 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_alter_student_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='question',
            fields=[
                ('question_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('question', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'question',
            },
        ),
    ]
