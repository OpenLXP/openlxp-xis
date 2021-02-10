from django.urls import path, include
from rest_framework.routers import DefaultRouter

from metadata_api import views

router = DefaultRouter()

urlpatterns = [
    path('metadata-ledger/', views.MetadataLedgerView.as_view())
]