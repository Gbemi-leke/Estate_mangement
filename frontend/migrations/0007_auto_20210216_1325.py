# Generated by Django 3.1.5 on 2021-02-16 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0006_auto_20210216_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='pro_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, max_length=100, verbose_name='Price'),
        ),
    ]
