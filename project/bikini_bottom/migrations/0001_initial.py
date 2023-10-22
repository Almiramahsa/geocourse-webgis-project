# Generated by Django 4.2.6 on 2023-10-22 03:41

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('types', models.CharField(choices=[('government', 'Pemerintahan'), ('public', 'Fasilitas Umum'), ('park', 'Taman'), ('restaurant', 'Restoran'), ('shop', 'Toko')], max_length=20)),
                ('status', models.CharField(choices=[('proposed', 'Proposed'), ('under_review', 'Under Review'), ('planned', 'Planned'), ('cancelled', 'Cancelled'), ('construction', 'Under Construction'), ('completed', 'Completed')], default='proposed', max_length=20)),
                ('open', models.BooleanField(default=False)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_unit', models.CharField(choices=[('hourly', 'Per Jam'), ('daily', 'Per Hari'), ('monthly', 'Per Bulan'), ('annual', 'Per Tahun')], max_length=20)),
                ('photo', models.ImageField(upload_to='facility')),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
