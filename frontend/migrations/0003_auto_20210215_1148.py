# Generated by Django 3.1.5 on 2021-02-15 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_auto_20210210_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='agents',
            name='buy_contact',
            field=models.CharField(default=1, max_length=100, verbose_name='Contact'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buy',
            name='buy_contact',
            field=models.CharField(default=1, max_length=100, verbose_name='Contact'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='buy_contact',
            field=models.CharField(default=1, max_length=100, verbose_name='Contact'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rent',
            name='buy_contact',
            field=models.CharField(default=1, max_length=100, verbose_name='Contact'),
            preserve_default=False,
        ),
    ]
