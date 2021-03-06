# Generated by Django 4.0 on 2021-12-08 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Roster', '0004_orksunit_weapons'),
    ]

    operations = [
        migrations.AddField(
            model_name='elfunit',
            name='armor',
            field=models.ManyToManyField(null=True, to='Roster.Armor'),
        ),
        migrations.AddField(
            model_name='elfunit',
            name='weapons',
            field=models.ManyToManyField(null=True, to='Roster.Weapon'),
        ),
        migrations.AddField(
            model_name='orksunit',
            name='armor',
            field=models.ManyToManyField(null=True, to='Roster.Armor'),
        ),
    ]
