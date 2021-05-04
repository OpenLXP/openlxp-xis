from django.urls import path
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()

urlpatterns = [
    path('metadata-ledger/', views.MetadataLedgerView.as_view()),
    path('metadata/', views.MetadataLedgerView.as_view(), name="metadata"),
    path('catalogs/', views.get_course_providers),
    path('composite-ledger/', views.CompositeLedgerView.as_view(
        {'get': 'records_for_provider_name'}),
         name='records_for_provider_name'),
    path('composite-ledger/<str:course_id>/', views.CompositeLedgerView.as_view(
        {'get': 'record_for_requested_course_id'}),
         name='record_for_requested_course_id'),
]
