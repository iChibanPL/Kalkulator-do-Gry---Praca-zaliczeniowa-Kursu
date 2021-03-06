# Generated by Django 4.0 on 2021-12-08 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Roster', '0007_customunitork_customunitelf'),
    ]

    operations = [
        migrations.AddField(
            model_name='customunitork',
            name='amount',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customunitork',
            name='total_points',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='armor',
            name='point_value',
            field=models.PositiveSmallIntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='elfunit',
            name='point_value',
            field=models.PositiveSmallIntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='orksunit',
            name='point_value',
            field=models.PositiveSmallIntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='name',
            field=models.PositiveSmallIntegerField(max_length=100),
        ),
    ]
