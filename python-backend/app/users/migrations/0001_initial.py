'''Generated by Django 4.2.3 on 2023-07-23 09:03'''

from django.db import migrations, models


class Migration(migrations.Migration):
    '''Create table USERS'''
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='USERS',
            fields=[
                ('tg_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
    ]
