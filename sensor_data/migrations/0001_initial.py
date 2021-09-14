# Generated by Django 3.2.7 on 2021-09-14 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor_Type',
            fields=[
                ('short', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('long', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='sensor_full_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daq', models.IntegerField()),
                ('module_nr', models.IntegerField()),
                ('slot', models.IntegerField()),
                ('ch_nr', models.IntegerField()),
                ('sensor_name', models.CharField(max_length=50)),
                ('serial', models.IntegerField()),
                ('property', models.CharField(max_length=50)),
                ('color_code', models.CharField(max_length=10)),
                ('MP_TP_TW', models.CharField(max_length=3)),
                ('tdms_group', models.CharField(max_length=20)),
                ('level_name', models.CharField(max_length=5)),
                ('level_lat_Exact', models.DecimalField(decimal_places=3, max_digits=10)),
                ('level_lat_round_or_name', models.IntegerField()),
                ('heading', models.IntegerField()),
                ('orientation', models.CharField(max_length=2)),
                ('sensor_part_nr', models.IntegerField()),
                ('status', models.IntegerField()),
                ('sensor_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensor_data.sensor_type')),
            ],
        ),
    ]