# Generated by Django 2.0.2 on 2018-04-25 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20180426_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='response',
            field=models.CharField(max_length=1000),
        ),
    ]
