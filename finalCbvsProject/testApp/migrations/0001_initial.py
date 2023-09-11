# Generated by Django 4.2.2 on 2023-07-26 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('taste', models.CharField(max_length=70)),
                ('color', models.CharField(max_length=70)),
                ('price', models.FloatField()),
            ],
        ),
    ]