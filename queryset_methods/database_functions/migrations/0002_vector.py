# Generated by Django 4.1.7 on 2023-04-04 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_functions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
            ],
        ),
    ]
