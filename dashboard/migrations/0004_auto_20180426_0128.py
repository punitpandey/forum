# Generated by Django 2.0.2 on 2018-04-25 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_response_responsedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='status',
            field=models.CharField(default='Active', max_length=10),
        ),
    ]
