# Generated by Django 4.2.2 on 2023-07-03 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsInfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BengaluruJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('company', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=20)),
                ('eligibility', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('PhoneNumber', models.BigIntegerField()),
            ],
        ),
    ]
