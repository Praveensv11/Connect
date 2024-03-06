# Generated by Django 4.2.4 on 2024-03-06 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0005_alter_event_info_host_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat', models.CharField(default='', max_length=10000)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name', to='event_app.event_info')),
            ],
        ),
    ]