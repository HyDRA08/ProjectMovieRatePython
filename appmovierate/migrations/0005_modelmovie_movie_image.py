# Generated by Django 2.1.7 on 2019-04-25 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmovierate', '0004_auto_20190425_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelmovie',
            name='movie_image',
            field=models.FileField(default='', upload_to='images/'),
        ),
    ]
