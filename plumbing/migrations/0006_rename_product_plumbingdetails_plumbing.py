# Generated by Django 5.0 on 2023-12-09 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plumbing', '0005_alter_plumbing_link_alter_plumbing_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plumbingdetails',
            old_name='product',
            new_name='plumbing',
        ),
    ]