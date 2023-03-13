# Generated by Django 4.1.7 on 2023-03-10 09:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_ts', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_ts', models.DateTimeField(auto_now=True, verbose_name='Last Updated Date')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('country_code', models.CharField(max_length=5, unique=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_created_related', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_updated_related', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('name', 'country_code')},
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_ts', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_ts', models.DateTimeField(auto_now=True, verbose_name='Last Updated Date')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('country_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country_cities', to='masters.country')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_created_related', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_updated_related', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
