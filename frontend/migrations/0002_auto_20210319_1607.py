# Generated by Django 3.1.5 on 2021-03-19 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addproperty',
            name='add_price',
            field=models.IntegerField(verbose_name='Price'),
        ),
    ]
