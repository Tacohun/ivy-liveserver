# Generated by Django 3.1.1 on 2020-10-07 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magazines', '0008_auto_20201007_1009'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SalesSummary',
        ),
    ]