# Generated by Django 2.1.2 on 2018-10-19 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20181019_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='chargemap.Country'),
        ),
    ]