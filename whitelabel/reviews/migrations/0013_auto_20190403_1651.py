# Generated by Django 2.1.7 on 2019-04-03 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0012_auto_20190403_1344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='softwareproduct',
            name='company_logo',
        ),
        migrations.RemoveField(
            model_name='softwareproduct',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='softwareproduct',
            name='website',
        ),
    ]
