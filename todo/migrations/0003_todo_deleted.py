# Generated by Django 3.0.5 on 2020-04-20 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20200419_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
