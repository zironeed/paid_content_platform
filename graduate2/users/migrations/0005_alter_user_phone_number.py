# Generated by Django 4.2.5 on 2023-09-17 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True, verbose_name='User_phone (without +7)'),
        ),
    ]
