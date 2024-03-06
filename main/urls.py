from django.urls import path
from .views import *


urlpatterns = [
    path('get_banner/', get_banner),
    path('get_servisec/', get_services),
    path('get_testimonal/', get_testimonial),
    path('get_about/', get_about),
    path('get_portfolio/', get_portfolio),
    path('get_client/', get_clients),
    path('create_contact/', create_contact),
]
