# Generated by Django 2.2 on 2019-04-16 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
        ('genre', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='book',
            field=models.ManyToManyField(to='book.Book'),
        ),
    ]