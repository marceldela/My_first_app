# Generated by Django 3.0.3 on 2020-03-05 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excel', '0014_auto_20200305_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexpackage',
            name='index',
            field=models.FloatField(),
        ),
    ]
