# Generated by Django 2.2 on 2019-04-26 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suborder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suborder',
            name='order_id',
        ),
    ]
