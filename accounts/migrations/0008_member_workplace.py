# Generated by Django 3.0.5 on 2020-12-26 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20201222_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='workplace',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
