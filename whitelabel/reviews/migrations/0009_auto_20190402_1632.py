# Generated by Django 2.1.7 on 2019-04-02 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0008_auto_20190402_1627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='softwareproduct',
            old_name='website_link',
            new_name='website',
        ),
        migrations.AddField(
            model_name='softwareproduct',
            name='company_name',
            field=models.CharField(default='Company Name', max_length=150),
            preserve_default=False,
        ),
    ]
