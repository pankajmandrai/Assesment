# Generated by Django 3.0.5 on 2020-11-13 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app23', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='details_description',
            field=models.CharField(blank=True, max_length=10000),
        ),
    ]