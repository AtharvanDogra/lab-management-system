# Generated by Django 3.2.9 on 2021-12-29 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20211229_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='userleavestaken',
            name='year',
            field=models.IntegerField(default=True),
        ),
    ]
