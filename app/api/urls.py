from django.urls import path
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()

app_name = 'api'

urlpatterns = [
    path('metadata/', views.metadata_list,
         name='metadata'),
    path('supplemental-data/', views.create_supplemental_metadata_record,
         name='supplemental-data'),
    path('catalogs/', views.get_course_providers),
    path('metadata/<str:course_id>/', views.record_for_requested_course_id,
         name='record_for_requested_course_id'),
    path('xis-workflow/', views.xis_workflow_api),
    # path('post_to_neo4j/', views.post_to_neo4j,
    #      name='post_to_neo4j'),
]
