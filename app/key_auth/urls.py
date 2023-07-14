from django.urls import path
from key_auth import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

app_name = 'key_auth'

urlpatterns = [
    path('generate-key/',
         views.GenerateAPIKeyFromOtherAuthMethod.as_view(), name='gen-key'),
    path('delete-key/', views.LogoutView.as_view(), name='delete-key'),
    path('delete-all-keys/', views.LogoutAllView.as_view(),
         name='delete-all-keys'),
]
