from django.urls import path

from .views import lead_list, lead_detail, lead_create, lead_update, lead_delete

app_name = "leads"


urlpatterns = [
    path('',lead_list, name= 'lead_list'),                          # http://127.0.0.1:8000/leads/              - default leads landing page 
    path('create/', lead_create, name= 'lead_create'),              # http://127.0.0.1:8000/leads/create/
    path('<int:pk>/', lead_detail, name= 'lead_detail'),            # http://127.0.0.1:8000/leads/1/            - shows details for each lead 
    path('<int:pk>/update/',lead_update, name= 'lead_update'),      # http://127.0.0.1:8000/leads/1/update/ 
    path('<int:pk>/delete/', lead_delete, name= 'lead_delete')      # http://127.0.0.1:8000/leads/1/delete/ 
]