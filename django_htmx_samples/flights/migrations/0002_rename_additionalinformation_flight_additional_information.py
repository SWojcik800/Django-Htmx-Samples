# Generated by Django 4.2.4 on 2023-08-24 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flight',
            old_name='additionalInformation',
            new_name='additional_information',
        ),
    ]
