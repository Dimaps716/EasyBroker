from django.apps import AppConfig


class BrokerConfig(AppConfig):
  default_auto_field = 'django.db.models.BigAutoField'
  name = 'Broker'

  def ready(self):
    import bukeala.signals