# Generated by Django 3.1.3 on 2020-11-11 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magazines', '0025_remove_magazine_purchasecount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='magazine',
            old_name='description2',
            new_name='feature',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='magazine',
            name='price',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]