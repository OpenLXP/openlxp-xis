from django.urls import path
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()

urlpatterns = [
    path('metadata-ledger/', views.MetadataLedgerView.as_view()),
    path('metadata/', views.MetadataLedgerView.as_view(), name="metadata"),
]

