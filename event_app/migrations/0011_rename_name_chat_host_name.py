# Generated by Django 4.2.4 on 2024-03-06 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0010_alter_chat_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='name',
            new_name='Host_name',
        ),
    ]
