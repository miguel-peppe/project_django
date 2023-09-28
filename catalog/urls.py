from django.urls import path
from catalog.views import start, dashboard


urlpatterns = [

    path('', start),
    path('dash', dashboard)
]
