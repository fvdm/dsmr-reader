# Generated by Django 2.2 on 2019-04-19 08:19

from django.db import migrations
from django.utils.translation import ugettext_lazy


def migrate_forward(apps, schema_editor):
    """ Notify user about the new graphs. """
    import dsmr_frontend.services
    import dsmr_backend.services

    if dsmr_backend.services.is_recent_installation():
        # Skip for new installations.
        return

    Notification = apps.get_model('dsmr_frontend', 'Notification')
    Notification.objects.create(
        message=dsmr_frontend.services.get_translated_string(text=ugettext_lazy(
            "DSMR-reader v2.0.0 adds security fixes and also marks the end of support for Python 3.4"
        )),
        redirect_to='frontend:changelog-redirect'
    )

def migrate_backward(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('dsmr_frontend', '0015_notification_meta'),
    ]

    operations = [
        migrations.RunPython(migrate_forward, migrate_backward),
    ]
