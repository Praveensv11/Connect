# Generated by Django 4.2.4 on 2024-03-07 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0012_remove_chat_host_name_chat_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('victim', models.CharField(default='', max_length=64)),
                ('reported_user', models.CharField(default='', max_length=64)),
                ('report', models.CharField(default='', max_length=1000)),
            ],
        ),
    ]
