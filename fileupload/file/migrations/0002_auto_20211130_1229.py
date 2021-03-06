# Generated by Django 3.2.9 on 2021-11-30 06:59

from django.db import migrations, models
import file.models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='files',
            field=models.FileField(blank=True, upload_to="Picture"),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, upload_to="Picture"),
        ),
    ]
