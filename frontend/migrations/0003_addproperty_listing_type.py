# Generated by Django 3.1.5 on 2021-03-22 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_auto_20210319_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='addproperty',
            name='listing_type',
            field=models.CharField(default=1, max_length=40, verbose_name='Listing Type'),
            preserve_default=False,
        ),
    ]