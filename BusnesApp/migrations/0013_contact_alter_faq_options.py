# Generated by Django 5.0.7 on 2024-08-04 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BusnesApp', '0012_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('call_center', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contact',
            },
        ),
        migrations.AlterModelOptions(
            name='faq',
            options={'verbose_name': 'FAQ', 'verbose_name_plural': 'FAQ'},
        ),
    ]
