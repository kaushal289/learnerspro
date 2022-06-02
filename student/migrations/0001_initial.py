# Generated by Django 4.0 on 2022-06-02 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('student_firstname', models.CharField(max_length=100)),
                ('student_lastname', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('last_login', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]
