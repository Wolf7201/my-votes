# Generated by Django 4.1.13 on 2023-12-06 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_event_start_date_alter_poll_event_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vote',
            old_name='invitation_code',
            new_name='anon_user',
        ),
    ]
