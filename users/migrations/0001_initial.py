# Generated by Django 2.1.2 on 2018-10-18 22:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chargemap', '0006_auto_20181018_1511'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_image', models.ImageField(default='default.png', upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chargemap.City')),
                ('user_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chargemap.Country')),
            ],
        ),
    ]
