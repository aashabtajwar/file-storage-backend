# Generated by Django 3.2.15 on 2022-10-14 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='storage',
            field=models.BigIntegerField(default=0),
        ),
    ]