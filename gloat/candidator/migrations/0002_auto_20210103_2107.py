# Generated by Django 3.1.4 on 2021-01-03 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='name',
            field=models.CharField(default='No Name', max_length=30),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='skill',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
