from datetime import timedelta

from django.utils import timezone

from bukeala.models import Request


def create_request():
  page = 1
  limit = 20
  request = Request(
      page=page,
      limit=limit,
  )
  request.save()