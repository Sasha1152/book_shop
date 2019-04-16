# Generated by Django 2.2 on 2019-04-16 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('image', '0001_initial'),
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('year', models.PositiveSmallIntegerField(max_length=4)),
                ('pages', models.PositiveSmallIntegerField(max_length=5)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('quantity', models.PositiveSmallIntegerField(default=1, max_length=2)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='author.Author')),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='image.Image')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
