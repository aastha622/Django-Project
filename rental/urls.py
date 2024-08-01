from django.urls import path
from .views import CarListCreate, CarDetail, CustomerListCreate, CustomerDetail, RentalListCreate, RentalDetail
from . import views

urlpatterns = [
    path('cars/', CarListCreate.as_view(), name='car-list-create'),
    path('cars/<int:pk>/', CarDetail.as_view(), name='car-detail'),
    path('customers/', CustomerListCreate.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerDetail.as_view(), name='customer-detail'),
    path('rentals/', RentalListCreate.as_view(), name='rental-list-create'),
    path('rentals/<int:pk>/', RentalDetail.as_view(), name='rental-detail'),
     path('cars/download-image/<int:car_id>/', views.download_image, name='download-image'),
]
