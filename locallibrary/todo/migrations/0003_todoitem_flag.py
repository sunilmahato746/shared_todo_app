# Generated by Django 3.0.5 on 2020-05-09 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20200502_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='Flag',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
