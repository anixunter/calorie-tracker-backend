from core.apps.common.models import ActivityLog
from django.contrib.contenttypes.models import ContentType


def activity_log(actor, verb, target=None, data=None):
    """
    Helper function to create an ActivityLog entry.
    """
    #we dont log actions from anonymous users unless explicitly needed
    if not actor or not actor.is_authenticated:
        return
    
    ActivityLog.objects.create(
        actor=actor,
        verb=verb,
        target=target,
        data=data
    )