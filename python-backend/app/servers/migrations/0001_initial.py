'''Generated by Django 4.2.3 on 2023-07-23 09:03'''

from django.db import migrations, models


class Migration(migrations.Migration):
    '''Create_table servers'''
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SERVERS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=16)),
                ('ptr', models.CharField(max_length=200)),
            ],
        ),
    ]
