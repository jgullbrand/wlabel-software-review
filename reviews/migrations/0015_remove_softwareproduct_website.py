# Generated by Django 2.1.7 on 2019-04-03 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0014_softwareproduct_website'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='softwareproduct',
            name='website',
        ),
    ]