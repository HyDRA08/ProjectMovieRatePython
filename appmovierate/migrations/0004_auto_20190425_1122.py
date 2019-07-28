# Generated by Django 2.1.7 on 2019-04-25 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmovierate', '0003_modelmovie'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelmovie',
            name='movie_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='modelmovie',
            name='movie_id',
            field=models.IntegerField(max_length=10),
        ),
    ]
