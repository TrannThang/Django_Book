# Generated by Django 4.2.5 on 2023-09-05 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poem',
            name='excerpt',
            field=models.TextField(blank=True, null=True),
        ),
    ]
