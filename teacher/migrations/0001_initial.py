

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('teacher_firstname', models.CharField(max_length=100)),
                ('teacher_lastname', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=100)),
                ('last_login', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'teacher',
            },
        ),
    ]
