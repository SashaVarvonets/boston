# Generated by Django 2.0.7 on 2018-07-10 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_remove_album_album_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_logo',
            field=models.FileField(default=None, upload_to=''),
        ),
    ]
