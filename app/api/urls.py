from django.urls import path, include
from rest_framework.routers import DefaultRouter
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> 21f2f28 (added new core app; fixed secret key docker config)
=======
>>>>>>> d4f8b38 (Adding XIA to XIS metadata_ledger using REST_API.)
from api import views

router = DefaultRouter()

urlpatterns = [
<<<<<<< HEAD
<<<<<<< HEAD
    path('metadata-ledger/', views.MetadataLedgerView.as_view()),
    path('metadata/', views.MetadataLedgerView.as_view()),
]
=======
    path('metadata-ledger/', views.MetadataLedgerView.as_view())
=======
    path('metadata-ledger/', views.MetadataLedgerView.as_view()),
    path('metadata/', views.MetadataLedgerView.as_view()),
>>>>>>> d4f8b38 (Adding XIA to XIS metadata_ledger using REST_API.)
]
>>>>>>> 21f2f28 (added new core app; fixed secret key docker config)
