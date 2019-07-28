# Generated by Django 2.1.7 on 2019-04-29 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmovierate', '0006_remove_modelmovie_movie_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='modelrating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=20)),
                ('ratings', models.IntegerField(max_length=10)),
                ('review', models.CharField(max_length=255)),
            ],
        ),
    ]
