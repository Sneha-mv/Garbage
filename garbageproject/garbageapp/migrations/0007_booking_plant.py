# Generated by Django 4.2.14 on 2024-08-15 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garbageapp', '0006_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='plant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='garbageapp.plant'),
        ),
    ]
