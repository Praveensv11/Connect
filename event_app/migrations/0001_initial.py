# Generated by Django 4.2.4 on 2024-02-23 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='event_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Host_name', models.CharField(default='', max_length=64)),
                ('Event_details', models.CharField(default='', max_length=500)),
                ('Location', models.CharField(max_length=500)),
                ('Contact_details', models.CharField(max_length=500)),
            ],
        ),
    ]
