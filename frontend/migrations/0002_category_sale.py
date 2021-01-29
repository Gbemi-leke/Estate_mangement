# Generated by Django 3.0.3 on 2021-01-29 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('for_sale', models.CharField(blank=True, max_length=100, null=True, verbose_name='Sale')),
                ('for_rent', models.CharField(blank=True, max_length=100, null=True, verbose_name='Rent')),
            ],
            options={
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pst_img', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Image 3')),
                ('pst_title', models.CharField(max_length=100, verbose_name='Type of property')),
                ('price', models.PositiveIntegerField(verbose_name='Price')),
                ('bath', models.PositiveIntegerField(verbose_name='Num of Bathrooms')),
                ('restroom', models.PositiveIntegerField(verbose_name='Num of Toilets')),
                ('more', models.CharField(max_length=100, verbose_name='More information')),
                ('cat_id', models.ManyToManyField(to='frontend.Category', verbose_name='Category')),
            ],
        ),
    ]