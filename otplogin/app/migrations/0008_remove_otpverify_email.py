# Generated by Django 4.0 on 2021-12-24 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_user_rotp_alter_user_otp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otpverify',
            name='email',
        ),
    ]