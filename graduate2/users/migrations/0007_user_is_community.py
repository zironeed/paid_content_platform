# Generated by Django 4.2.5 on 2023-09-21 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_rename_paid_userpayment_is_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_community',
            field=models.BooleanField(default=False, verbose_name='User_is_community'),
        ),
    ]
