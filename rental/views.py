from rest_framework import generics
from .models import Car, Customer, Rental
from .serializers import CarSerializer, CustomerSerializer, RentalSerializer
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _

def download_image(request, car_id):
    try:
        car = get_object_or_404(Car, id=car_id)
        image_file = car.image.open()
        response = FileResponse(image_file, content_type='image/jpeg')
        response['Content-Disposition'] = f'attachment; filename="{car.image.name.split("/")[-1]}"'
        return response
    except Car.DoesNotExist:
        raise Http404("Car does not exist")


class CarListCreate(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CustomerListCreate(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
   
class RentalListCreate(generics.ListCreateAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

class RentalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
   