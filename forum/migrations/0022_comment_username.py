# Generated by Django 3.2.7 on 2021-09-08 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0021_auto_20210908_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.CharField(default='Anonymous', max_length=255),
        ),
    ]
