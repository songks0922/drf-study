# Generated by Django 4.0.6 on 2022-07-19 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('update_dt',)},
        ),
    ]
