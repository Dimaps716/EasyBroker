from django.db import models


class Request(models.Model):
  """
  represent request.
  """
  REPORT_UPLOAD_PATH = 'requests'

  INITIATED = 'INITIATED'
  EXTRACT_DATA = 'EXTRACT_DATA'
  WRITING_REPORT = 'WRITING_REPORT'
  FINALIZED = 'FINALIZED'
  ERROR = 'ERROR'

  CHOICES_STATUS_REQUEST = [
    (INITIATED, 'INITIATED'),
    (EXTRACT_DATA, 'EXTRACT_DATA'),
    (WRITING_REPORT, 'WRITING_REPORT'),
    (FINALIZED, 'FINALIZED'),
    (ERROR, 'ERROR')
  ]

  page = models.IntegerField(default=1)
  limit = models.IntegerField(default=20)
  status_request = models.CharField(
    choices=CHOICES_STATUS_REQUEST, default=INITIATED, max_length=15
  )
  error_message = models.CharField(max_length=200, null=True, blank=True)
  report = models.FileField(upload_to=REPORT_UPLOAD_PATH, null=True, blank=True)