# Generated by Django 4.0 on 2021-12-10 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('Roster', '0015_alter_army_total_points_alter_customunitelf_army'),
    ]

    operations = [
        migrations.AddField(
            model_name='army',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
