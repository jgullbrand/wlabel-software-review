# Generated by Django 2.1.7 on 2019-04-02 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0009_auto_20190402_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='softwareproduct',
            name='company_logo',
            field=models.ImageField(default='default.jpg', upload_to='company_pics'),
        ),
    ]
