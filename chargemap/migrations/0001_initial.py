# Generated by Django 2.1.1 on 2018-10-02 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('house_number', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ChargeStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charge_station_name', models.CharField(max_length=100)),
                ('charge_station_operator', models.CharField(max_length=100)),
                ('charge_station_maxpower', models.IntegerField()),
                ('charge_station_score', models.FloatField()),
                ('charge_station_description', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ChargeStationAvailability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charge_station_available', models.CharField(default='No data', max_length=100)),
                ('charge_station_not_available', models.CharField(default='No data', max_length=100)),
                ('charge_station_not_data', models.CharField(default='No data', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ChargeStationPlugType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plug_type_1', models.CharField(max_length=100)),
                ('plug_type_2', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='chargestation',
            name='charge_station_plug',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='chargemap.ChargeStationPlugType'),
        ),
        migrations.AddField(
            model_name='chargestation',
            name='charge_station_status',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='chargemap.ChargeStationAvailability'),
        ),
        migrations.AddField(
            model_name='address',
            name='charge_station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chargemap.ChargeStation'),
        ),
    ]
