# Generated by Django 4.0 on 2021-12-09 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Roster', '0012_customunitelf_amount_customunitelf_total_points_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='army',
            name='total_points',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
