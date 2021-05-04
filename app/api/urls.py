from django.urls import path
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()

app_name = 'api'

urlpatterns = [
    path('metadata-ledger/', views.MetadataLedgerView.as_view()),
    path('metadata/', views.MetadataLedgerView.as_view(), name="metadata"),
    path('catalogs/', views.get_course_providers),
    path('composite-ledger/', views.CompositeLedgerView.as_view(
        {'get': 'get_records'}),
         name='get-records'),
    path('composite-ledger/<str:course_id>/', views.CompositeLedgerView.
         as_view({'get': 'record_for_requested_course_id'}),
         name='record_for_requested_course_id'),
]
