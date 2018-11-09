# Generated by Django 2.1.2 on 2018-10-23 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20181022_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='balance',
            field=models.FloatField(default=0, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='billing',
            name='bonus_balance',
            field=models.FloatField(default=0, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='billing',
            name='cunsumed_power',
            field=models.FloatField(default=0, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='billing',
            name='number_of_charges',
            field=models.IntegerField(default=0, null=True),
        ),
    ]