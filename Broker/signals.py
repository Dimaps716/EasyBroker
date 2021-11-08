from django.db.models.signals import post_save
from django.dispatch import receiver

from bukeala.models import Request
from bukeala.tasks.tasks_sync import sync_data


@receiver(post_save, sender=Request)
def process_request(sender, instance, created, **kwargs):
  if created:
    sync_data(instance.pk)
