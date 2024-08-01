from django.db import models
from django.utils import timezone

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    image = models.FileField(upload_to='car_documents/', null=True, blank=True)
   

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100) 
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Rental(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rental_date = models.DateTimeField(default=timezone.now)
    return_date = models.DateTimeField(null=True, blank=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('completed', 'Completed'), ('canceled', 'Canceled')], default='active')
    pickup_location = models.CharField(max_length=255, null=True, blank=True)
    dropoff_location = models.CharField(max_length=255, null=True, blank=True)
    insurance_opted = models.BooleanField(default=False)
    additional_driver = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)
    aadhar = models.FileField(upload_to='rental_documents/', null=True, blank=True)  # New field for file uploads
    rating = models.PositiveIntegerField()
 
    def __str__(self):
        return f"Rental of {self.car} by {self.customer}"