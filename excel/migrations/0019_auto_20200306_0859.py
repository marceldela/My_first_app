# Generated by Django 3.0.3 on 2020-03-06 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('excel', '0018_auto_20200306_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexpackage',
            name='pakiet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='excel.Package'),
        ),
    ]
