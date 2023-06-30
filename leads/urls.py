from django.urls import path

from .views import lead_list, lead_detail, lead_create

app_name = "leads"


urlpatterns = [
    path('',lead_list),                 # http://127.0.0.1:8000/leads/              - default leads landing page 
    path('create/', lead_create),       # http://127.0.0.1:8000/leads/create/
    path('<int:pk>/', lead_detail)      # http://127.0.0.1:8000/leads/1/            - shows details for each lead 
]