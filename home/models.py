
from django.db import models
from django.contrib.auth.models import User


# =========================================================
# SERVICE
# =========================================================

class Service(models.Model):

    CATEGORY_CHOICES = [
        ("Washing", "Washing"),
        ("Cleaning", "Cleaning"),
        ("Detailing", "Detailing"),
        ("Protection", "Protection"),
        ("Maintenance", "Maintenance"),
        ("Other", "Other"),
    ]

    name = models.CharField(
        max_length=150
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="Other"
    )

    description = models.TextField(
        blank=True
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    duration = models.CharField(
        max_length=100,
        blank=True
    )

    image = models.ImageField(
        upload_to="services/",
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


# =========================================================
# SPARE PART
# =========================================================

class SparePart(models.Model):

    name = models.CharField(
        max_length=150
    )

    part_number = models.CharField(
        max_length=100,
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    stock = models.PositiveIntegerField(
        default=0
    )

    image = models.ImageField(
        upload_to="spare_parts/",
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


# =========================================================
# VEHICLE
# =========================================================

class Vehicle(models.Model):

    FUEL_CHOICES = [
        ("Petrol", "Petrol"),
        ("Diesel", "Diesel"),
        ("CNG", "CNG"),
        ("Electric", "Electric"),
        ("Hybrid", "Hybrid"),
        ("Other", "Other"),
    ]

    VEHICLE_TYPE_CHOICES = [
        ("Hatchback", "Hatchback"),
        ("Sedan", "Sedan"),
        ("SUV", "SUV"),
        ("MUV", "MUV"),
        ("MPV", "MPV"),
        ("Coupe", "Coupe"),
        ("Convertible", "Convertible"),
        ("Pickup Truck", "Pickup Truck"),
        ("Other", "Other"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="vehicles"
    )

    vehicle_number = models.CharField(
        max_length=20
    )

    vehicle_type = models.CharField(
        max_length=50,
        choices=VEHICLE_TYPE_CHOICES,
        default="Other"
    )

    brand = models.CharField(
        max_length=100
    )

    model = models.CharField(
        max_length=100
    )

    year = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    fuel_type = models.CharField(
        max_length=30,
        choices=FUEL_CHOICES,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return (
            f"{self.vehicle_number} - "
            f"{self.brand} {self.model}"
        )


# =========================================================
# BOOKING
# =========================================================

class Booking(models.Model):

    VEHICLE_TYPE_CHOICES = [
        ("Hatchback", "Hatchback"),
        ("Sedan", "Sedan"),
        ("SUV", "SUV"),
        ("MUV", "MUV"),
        ("MPV", "MPV"),
        ("Coupe", "Coupe"),
        ("Convertible", "Convertible"),
        ("Pickup Truck", "Pickup Truck"),
        ("Other", "Other"),
    ]

    FUEL_CHOICES = [
        ("Petrol", "Petrol"),
        ("Diesel", "Diesel"),
        ("CNG", "CNG"),
        ("Electric", "Electric"),
        ("Hybrid", "Hybrid"),
        ("Other", "Other"),
    ]

    STATUS_CHOICES = [
        ("Booked", "Booked"),
        ("Confirmed", "Confirmed"),
        ("Vehicle Received", "Vehicle Received"),
        ("Service in Progress", "Service in Progress"),
        ("Ready", "Ready"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    ]

    PAYMENT_CHOICES = [
        ("Pending", "Pending"),
        ("Paid", "Paid"),
        ("Cash", "Cash"),
        ("Failed", "Failed"),
    ]

    # =====================================================
    # CUSTOMER DETAILS
    # =====================================================

    customer_name = models.CharField(
        max_length=150,
        blank=True,
        default=""
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        default=""
    )

    # =====================================================
    # VEHICLE DETAILS
    # =====================================================

    vehicle_number = models.CharField(
        max_length=20,
        blank=True,
        default=""
    )

    vehicle_type = models.CharField(
        max_length=50,
        choices=VEHICLE_TYPE_CHOICES,
        blank=True,
        default="Other"
    )

    vehicle_brand = models.CharField(
        max_length=100,
        blank=True,
        default=""
    )

    vehicle_model = models.CharField(
        max_length=100,
        blank=True,
        default=""
    )

    vehicle_year = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    fuel_type = models.CharField(
        max_length=30,
        choices=FUEL_CHOICES,
        blank=True,
        default=""
    )

    # =====================================================
    # SERVICE DETAILS
    # =====================================================

    service = models.ForeignKey(
        Service,
        on_delete=models.PROTECT,
        related_name="bookings"
    )

    booking_date = models.DateTimeField()

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    # =====================================================
    # BOOKING STATUS
    # =====================================================

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="Booked"
    )

    payment_status = models.CharField(
        max_length=30,
        choices=PAYMENT_CHOICES,
        default="Pending"
    )

    notes = models.TextField(
        blank=True
    )

    # =====================================================
    # TIMESTAMPS
    # =====================================================

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-booking_date"]

    def __str__(self):

        return (
            f"Booking #{self.id} - "
            f"{self.customer_name or 'Customer'} - "
            f"{self.vehicle_number or 'Vehicle'}"
        )


# =========================================================
# ORDER
# =========================================================

class Order(models.Model):

    STATUS_CHOICES = [
        ("Placed", "Placed"),
        ("Confirmed", "Confirmed"),
        ("Processing", "Processing"),
        ("Ready", "Ready"),
        ("Delivered", "Delivered"),
        ("Cancelled", "Cancelled"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="orders"
    )

    spare_part = models.ForeignKey(
        SparePart,
        on_delete=models.PROTECT,
        related_name="orders"
    )

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="part_orders"
    )

    quantity = models.PositiveIntegerField(
        default=1
    )

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="Placed"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):

        return (
            f"Order #{self.id} - "
            f"{self.spare_part.name}"
        )


# =========================================================
# CONTACT MESSAGE
# =========================================================

class ContactMessage(models.Model):

    name = models.CharField(
        max_length=150
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    subject = models.CharField(
        max_length=200,
        blank=True
    )

    message = models.TextField()

    is_read = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):

        return (
            f"{self.name} - "
            f"{self.subject or 'Contact Message'}"
        )
