"""api  URLs."""

# django
from django.urls import path

# views
from Broker import views

urlpatterns = [
    # url of the
    path(
        route='api/Properties-list/',
        view= views.PropertiesList,
        name= 'Properties_list'
    ),
    path(
        route='api/Properties-datail/<str:pk>/',
        view= views.PropertiesDetail,
        name= 'Properties_datail'
    )
  ]