# Generated by Django 3.0.3 on 2020-03-02 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excel', '0005_auto_20200302_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='period_cpp',
            name='CPP',
            field=models.IntegerField(null=True),
        ),
    ]
