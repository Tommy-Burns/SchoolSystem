# Generated by Django 3.2.9 on 2022-06-28 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='resources',
            field=models.URLField(blank=True),
        ),
    ]
