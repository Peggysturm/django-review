# Generated by Django 5.0 on 2023-12-09 08:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plumbing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя товара')),
                ('slug', models.SlugField(max_length=250)),
                ('link', models.URLField(max_length=250)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PlumbingDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('product', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='details', to='plumbing.plumbing', verbose_name='Детали')),
            ],
        ),
    ]