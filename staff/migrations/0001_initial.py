# Generated by Django 3.2.9 on 2022-06-30 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('expertise', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.IntegerField()),
                ('experience', models.IntegerField()),
            ],
        ),
    ]
