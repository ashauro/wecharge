# Generated by Django 2.1.2 on 2018-10-18 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20181018_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Car'),
        ),
    ]