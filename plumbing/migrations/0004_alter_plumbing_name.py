# Generated by Django 5.0 on 2023-12-09 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plumbing', '0003_alter_plumbingdetails_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plumbing',
            name='name',
            field=models.CharField(max_length=300, verbose_name='Имя товара'),
        ),
    ]
