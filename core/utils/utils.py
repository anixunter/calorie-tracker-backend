from core.utils.models import ActivityLog
from django.contrib.contenttypes.models import ContentType


def log_activity(actor, verb, target=None, data=None):
    """
    Helper function to create an ActivityLog entry.
    """
    ActivityLog.objects.create(
        actor=actor,
        verb=verb,
        target=target,
        data=data
    )