# Generated by Django 2.2.7 on 2019-12-05 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20191205_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='img',
            field=models.ImageField(blank=True, upload_to='profile/', verbose_name='Profile Picture'),
        ),
    ]