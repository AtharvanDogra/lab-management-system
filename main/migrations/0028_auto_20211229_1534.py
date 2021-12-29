# Generated by Django 3.2.9 on 2021-12-29 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_userleavestaken_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userleavestaken',
            name='Count',
        ),
        migrations.RemoveField(
            model_name='userleavestaken',
            name='year',
        ),
        migrations.AddField(
            model_name='userleavestaken',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userleavestaken',
            name='leave_taken',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.totalleaves'),
        ),
    ]
