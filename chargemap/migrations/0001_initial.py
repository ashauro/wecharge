# Generated by Django 2.1.2 on 2018-10-16 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChargeStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charge_station_name', models.CharField(max_length=100)),
                ('charge_station_latitude', models.FloatField(default=0, max_length=10)),
                ('charge_station_longtitude', models.FloatField(default=0, max_length=10)),
                ('charge_station_maxpower', models.IntegerField(default=0)),
                ('charge_station_score', models.FloatField(default=0.0)),
                ('charge_station_address', models.CharField(max_length=100, null=True)),
                ('charge_station_description', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ChargeStationPlugType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plug_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ChargeStationStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ChargeStationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ChargeStationWorkingTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('working_time', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StationOperator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operator', models.CharField(default=None, max_length=100)),
                ('site', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='chargemap.Country'),
        ),
        migrations.AddField(
            model_name='chargestation',
            name='charge_station_city',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='chargemap.City'),
        ),
        migrations.AddField(
            model_name='chargestation',
            name='charge_station_operator',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='chargemap.StationOperator'),
        ),
        migrations.AddField(
            model_name='chargestation',
            name='charge_station_plug',
            field=models.ManyToManyField(to='chargemap.ChargeStationPlugType'),
        ),
        migrations.AddField(
            model_name='chargestation',
            name='charge_station_status',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='chargemap.ChargeStationStatus'),
        ),
        migrations.AddField(
            model_name='chargestation',
            name='charge_station_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='chargemap.ChargeStationType'),
        ),
        migrations.AddField(
            model_name='chargestation',
            name='charge_station_working_time',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='chargemap.ChargeStationWorkingTime'),
        ),
    ]
