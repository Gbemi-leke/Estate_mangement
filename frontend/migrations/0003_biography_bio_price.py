# Generated by Django 3.1.5 on 2021-02-03 00:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_auto_20210202_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='biography',
            name='bio_price',
            field=models.PositiveIntegerField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]