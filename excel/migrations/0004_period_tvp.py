# Generated by Django 3.0.3 on 2020-03-02 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excel', '0003_period_tvn_max_min'),
    ]

    operations = [
        migrations.CreateModel(
            name='Period_TVP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('CPP', models.IntegerField()),
            ],
        ),
    ]