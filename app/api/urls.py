from django.urls import path
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()

app_name = 'api'

urlpatterns = [
    path('metadata/', views.metadata_list,
         name='metadata'),
    path('catalogs/', views.get_course_providers),
    path('metadata/<str:course_id>/', views.record_for_requested_course_id,
         name='record_for_requested_course_id'),
]
