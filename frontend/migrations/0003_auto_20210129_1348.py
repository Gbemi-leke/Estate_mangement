# Generated by Django 3.0.3 on 2021-01-29 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_category_sale'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='for_rent',
        ),
        migrations.AlterField(
            model_name='category',
            name='for_sale',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Sale or rent'),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('body', models.CharField(max_length=400)),
                ('f_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/', verbose_name='Image')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='frontend.Post')),
            ],
        ),
    ]
