import itertools
import json
import logging
import os
from datetime import datetime


import requests

from bukeala.models import Request, Properties

@task
def sync_data(request_id):
  request = Request.objects.get(pk=request_id)
  try:
    request.status_request = Request.EXTRACT_DATA
    request.save()
    with requests.Session() as s:
      payload = json.dumps({
        "page": request.page,
        "limit": request.limit,
        "hashKey": settings.EASYBROKER_HASHKEY,
        })
      response = s.post(
          url=settings.EASYBROKER_URL, data=payload,
          headers={'Content-Type': 'text/plain'}
        )
      response.raise_for_status()
      bookings = response.json().get("bookings")
      Properties.objects.bulk_create(
      bookings
      )
    generate_report(request_id)
  except Exception as err:
    logger.error("error: {}".format(str(err)))
    request.status_request = Request.ERROR
    request.error_message = str(err)
    request.save()
