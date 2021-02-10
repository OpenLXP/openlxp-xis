"""openlxp_xis_project URL Configuration
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> 86c1339 (django project set up with docker; sample api endpoint)
=======

>>>>>>> 68c08d4 (django project set up with docker and same api endpoint)
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    path('api/', include('api.urls'))
=======
    path('api/', include('metadata_api.urls'))
>>>>>>> 86c1339 (django project set up with docker; sample api endpoint)
=======
    path('api/', include('metadata_api.urls'))
>>>>>>> 68c08d4 (django project set up with docker and same api endpoint)
=======
    path('api/', include('api.urls'))
>>>>>>> 21f2f28 (added new core app; fixed secret key docker config)
]
