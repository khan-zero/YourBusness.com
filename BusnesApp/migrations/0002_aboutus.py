# Generated by Django 5.0.7 on 2024-08-04 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BusnesApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('opportunities', models.CharField(max_length=255)),
            ],
        ),
    ]
