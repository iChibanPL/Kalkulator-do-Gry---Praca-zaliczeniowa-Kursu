# Generated by Django 4.0 on 2021-12-09 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Roster', '0011_alter_customunitork_total_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='customunitelf',
            name='amount',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customunitelf',
            name='total_points',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customunitork',
            name='army',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Roster.army'),
        ),
    ]