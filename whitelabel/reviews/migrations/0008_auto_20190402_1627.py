# Generated by Django 2.1.7 on 2019-04-02 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_auto_20190402_1626'),
    ]

    operations = [
        migrations.RenameField(
            model_name='softwareproduct',
            old_name='image_logo',
            new_name='company_logo',
        ),
    ]
