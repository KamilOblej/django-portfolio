# Generated by Django 3.0.5 on 2020-10-07 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialIcon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.TextField()),
                ('icon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Icon')),
            ],
        ),
    ]
