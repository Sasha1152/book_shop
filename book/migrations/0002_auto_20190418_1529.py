# Generated by Django 2.2 on 2019-04-18 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.PositiveSmallIntegerField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='image.Image'),
        ),
        migrations.AlterField(
            model_name='book',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=1, max_length=2, null=True),
        ),
    ]