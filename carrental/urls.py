from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rental import views 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rental.urls')),  # Include the app's URL configurations
     path('download-image/<int:car_id>/', views.download_image, name='download-image'),
]



    



