# Generated by Django 5.1.7 on 2025-03-20 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session_year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_start', models.DateField()),
                ('session_end', models.DateField()),
            ],
        ),
    ]
