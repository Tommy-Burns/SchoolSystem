# Generated by Django 3.2.9 on 2022-06-30 16:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='staff/images/'),
            preserve_default=False,
        ),
    ]