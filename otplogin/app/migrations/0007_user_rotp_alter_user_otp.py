# Generated by Django 4.0 on 2021-12-24 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_otpverify_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Rotp',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='otp',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
    ]