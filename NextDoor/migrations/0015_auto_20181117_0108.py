# Generated by Django 2.1.2 on 2018-11-16 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NextDoor', '0014_auto_20181117_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
