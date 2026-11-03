from django.contrib import admin

from .models import (
    Service,
    SparePart,
    Vehicle,
    Booking,
    Order,
    ContactMessage,
)


# =========================================================
# SERVICE
# =========================================================

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "price",
        "duration",
        "is_active",
        "created_at",
    )

    list_filter = (
        "category",
        "is_active",
    )

    search_fields = (
        "name",
        "category",
        "description",
    )

    list_editable = (
        "price",
        "is_active",
    )

    ordering = (
        "name",
    )


# =========================================================
# SPARE PART
# =========================================================

@admin.register(SparePart)
class SparePartAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "part_number",
        "price",
        "stock",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
        "part_number",
        "description",
    )

    list_editable = (
        "price",
        "stock",
        "is_active",
    )

    ordering = (
        "name",
    )


# =========================================================
# VEHICLE
# =========================================================

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):

    list_display = (
        "vehicle_number",
        "brand",
        "model",
        "year",
        "fuel_type",
        "user",
        "created_at",
    )

    list_filter = (
        "brand",
        "fuel_type",
        "year",
    )

    search_fields = (
        "vehicle_number",
        "brand",
        "model",
        "user__username",
        "user__email",
    )

    autocomplete_fields = (
        "user",
    )

    ordering = (
        "-created_at",
    )


# =========================================================
# BOOKING
# =========================================================

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "customer_name",
        "phone",
        "vehicle_number",
        "vehicle_brand",
        "vehicle_model",
        "service",
        "booking_date",
        "amount",
        "status",
        "payment_status",
        "created_at",
    )

    list_filter = (
        "status",
        "payment_status",
        "service",
        "booking_date",
    )

    search_fields = (
        "customer_name",
        "phone",
        "vehicle_number",
        "vehicle_brand",
        "vehicle_model",
        "service__name",
    )

    list_editable = (
        "status",
        "payment_status",
    )

    autocomplete_fields = (
        "service",
    )

    readonly_fields = (
        "amount",
        "created_at",
        "updated_at",
    )

    date_hierarchy = "booking_date"

    ordering = (
        "-booking_date",
    )


# =========================================================
# ORDER
# =========================================================

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "spare_part",
        "vehicle",
        "quantity",
        "total_price",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "created_at",
    )

    search_fields = (
        "user__username",
        "user__email",
        "spare_part__name",
        "spare_part__part_number",
        "vehicle__vehicle_number",
    )

    list_editable = (
        "status",
    )

    autocomplete_fields = (
        "user",
        "spare_part",
        "vehicle",
    )

    readonly_fields = (
        "total_price",
        "created_at",
        "updated_at",
    )

    ordering = (
        "-created_at",
    )


# =========================================================
# CONTACT MESSAGES
# =========================================================

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "phone",
        "subject",
        "is_read",
        "created_at",
    )

    list_filter = (
        "is_read",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "phone",
        "subject",
        "message",
    )

    list_editable = (
        "is_read",
    )

    readonly_fields = (
        "created_at",
    )

    ordering = (
        "-created_at",
    )