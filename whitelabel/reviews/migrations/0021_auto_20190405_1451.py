# Generated by Django 2.1.7 on 2019-04-05 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0020_auto_20190405_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='softwareproduct',
            name='product_website',
            field=models.URLField(blank=True, null=True, verbose_name='Product website (add https://)'),
        ),
    ]
