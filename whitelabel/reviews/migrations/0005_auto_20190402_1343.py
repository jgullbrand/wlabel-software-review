# Generated by Django 2.1.7 on 2019-04-02 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20190401_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_url',
            field=models.SlugField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='softwareproduct',
            name='image_logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
