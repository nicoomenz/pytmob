# Generated by Django 2.2.28 on 2022-09-16 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redirect',
            name='key',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
