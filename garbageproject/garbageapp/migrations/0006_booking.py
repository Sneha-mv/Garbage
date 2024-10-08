# Generated by Django 4.2.14 on 2024-08-13 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garbageapp', '0005_plant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('place', models.CharField(max_length=50)),
                ('waste_type', models.CharField(choices=[('bio-degradable', 'Bio-degradable'), ('non-biodegradable', 'Non-biodegradable'), ('hazardous', 'Hazardous')], max_length=20)),
                ('weight', models.PositiveIntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
    ]
