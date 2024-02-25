# Generated by Django 4.2.4 on 2024-02-24 05:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_info',
            name='Host_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
