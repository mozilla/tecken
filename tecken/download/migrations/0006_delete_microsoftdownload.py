# Generated by Django 2.2.12 on 2020-05-28 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('download', '0005_msdownload_on_delete_null_upload'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MicrosoftDownload',
        ),
    ]