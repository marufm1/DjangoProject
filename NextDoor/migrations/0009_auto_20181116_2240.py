# Generated by Django 2.1.3 on 2018-11-16 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NextDoor', '0008_auto_20181116_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='date',
            field=models.DateField(verbose_name='Date'),
        ),
    ]