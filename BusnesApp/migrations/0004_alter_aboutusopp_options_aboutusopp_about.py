# Generated by Django 5.0.7 on 2024-08-04 09:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BusnesApp', '0003_aboutusopp_alter_aboutus_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutusopp',
            options={'verbose_name': 'AboutUsOpp', 'verbose_name_plural': 'AboutUsOpp'},
        ),
        migrations.AddField(
            model_name='aboutusopp',
            name='about',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='BusnesApp.aboutus'),
            preserve_default=False,
        ),
    ]
