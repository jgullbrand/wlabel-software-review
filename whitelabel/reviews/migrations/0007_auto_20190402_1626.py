# Generated by Django 2.1.7 on 2019-04-02 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_auto_20190402_1611'),
    ]

    operations = [
        migrations.RenameField(
            model_name='softwareproduct',
            old_name='free_trial',
            new_name='free_trial_offered',
        ),
        migrations.AlterField(
            model_name='softwareproduct',
            name='pricing_details',
            field=models.TextField(),
        ),
    ]
