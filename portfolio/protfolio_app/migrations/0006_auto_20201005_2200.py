# Generated by Django 3.0.5 on 2020-10-05 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protfolio_app', '0005_auto_20201005_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='pub_date',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
