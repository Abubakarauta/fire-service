# Generated by Django 4.1.4 on 2022-12-10 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NationalFireAcademy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Academy')),
            ],
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Operations')),
                ('operationType', models.CharField(choices=[('FireFighting', 'firefighting'), ('EffectiveRescues', 'effectiverescues'), ('topographyAllocatedAreas', 'topographyAllocatedAreas')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rank', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=50)),
                ('staffId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Stations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Stations')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('station_description', models.TextField()),
                ('date_created', models.DateField()),
                ('emergencyNumber', models.CharField(max_length=50)),
                ('head_of_station', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Department.staff')),
            ],
        ),
    ]
