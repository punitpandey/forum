# Generated by Django 2.0.2 on 2018-04-25 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='lastactivedate',
            field=models.DateField(default='2018-04-26'),
        ),
        migrations.AddField(
            model_name='query',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
