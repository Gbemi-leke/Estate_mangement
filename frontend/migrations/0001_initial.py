# Generated by Django 3.1.5 on 2021-03-06 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_img', models.ImageField(blank=True, default='', null=True, upload_to='uploads/', verbose_name='Profile Image')),
                ('agent_title', models.CharField(max_length=100, verbose_name='Profile Title')),
                ('agent_desription', models.TextField(verbose_name='Description')),
                ('agent_contact', models.CharField(max_length=20, verbose_name='Contact')),
                ('agent_address', models.CharField(max_length=100, verbose_name='Address')),
                ('agent_email', models.EmailField(max_length=50, verbose_name='Email')),
            ],
            options={
                'verbose_name_plural': 'Agents',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_image', models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name='User Image')),
                ('user_name', models.CharField(max_length=150, verbose_name='User Name')),
                ('user_number', models.CharField(max_length=20, verbose_name='Founder Number')),
                ('user_email', models.EmailField(max_length=150, verbose_name='Founder Email')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_img', models.ImageField(blank=True, default='', null=True, upload_to='uploads/', verbose_name='Profile Image')),
                ('pro_title', models.CharField(max_length=100, verbose_name='Profile Title')),
                ('pro_sale', models.CharField(max_length=20, verbose_name='Sales or Rent')),
                ('pro_price', models.CharField(max_length=20, verbose_name='Price')),
                ('pro_desription', models.TextField(verbose_name='Description')),
                ('pro_contact', models.CharField(max_length=20, verbose_name='Contact')),
                ('pro_date', models.DateTimeField(auto_now_add=True)),
                ('property_type', models.CharField(choices=[('S', 'Sponsored'), ('F', 'Featured'), ('B', 'Buy'), ('R', 'Rent'), ('', 'Please Choose')], default='', max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Property',
            },
        ),
        migrations.CreateModel(
            name='AddProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_img', models.ImageField(blank=True, default='', null=True, upload_to='uploads/', verbose_name='Profile Image')),
                ('add_title', models.CharField(max_length=100, verbose_name='Profile Title')),
                ('add_price', models.CharField(max_length=20, verbose_name='Price')),
                ('add_desription', models.TextField(verbose_name='Description')),
                ('add_contact', models.CharField(max_length=20, verbose_name='Contact')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('property_type', models.CharField(choices=[('B', 'Buy'), ('R', 'Rent'), ('', 'Please Choose')], default='', max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'AddProperty',
            },
        ),
    ]
