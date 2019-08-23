# Generated by Django 2.2.4 on 2019-08-19 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cabData',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=50)),
                ('vehicle_model_id', models.CharField(max_length=50, null=True)),
                ('package_id', models.CharField(max_length=50, null=True)),
                ('travel_type_id', models.CharField(max_length=50, null=True)),
                ('from_area_id', models.CharField(max_length=50, null=True)),
                ('to_area_id', models.CharField(max_length=50, null=True)),
                ('from_city_id', models.CharField(max_length=50, null=True)),
                ('to_city_id', models.CharField(max_length=50, null=True)),
                ('from_date', models.CharField(max_length=50, null=True)),
                ('to_date', models.CharField(max_length=50, null=True)),
                ('online_booking', models.IntegerField(max_length=1, null=True)),
                ('mobile_site_booking', models.IntegerField(max_length=1, null=True)),
                ('booking_created', models.CharField(max_length=50, null=True)),
                ('from_lat', models.CharField(max_length=50, null=True)),
                ('from_long', models.CharField(max_length=50, null=True)),
                ('to_lat', models.CharField(max_length=50, null=True)),
                ('to_long', models.CharField(max_length=50, null=True)),
                ('car_cancellation', models.IntegerField(max_length=1, null=True)),
            ],
        ),
    ]