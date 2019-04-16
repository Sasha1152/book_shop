# Generated by Django 2.2 on 2019-04-16 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=64)),
                ('last_name', models.CharField(blank=True, max_length=64)),
                ('biography', models.TextField()),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='image.Image')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
