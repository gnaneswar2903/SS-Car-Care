
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import (
    Vehicle,
    Booking,
    ContactMessage,
)


# =========================================================
# CUSTOMER REGISTRATION
# =========================================================

class RegisterForm(UserCreationForm):

    first_name = forms.CharField(
        max_length=100,
        required=True
    )

    last_name = forms.CharField(
        max_length=100,
        required=False
    )

    email = forms.EmailField(
        required=True
    )

    class Meta:
        model = User

        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]

    def save(self, commit=True):

        user = super().save(commit=False)

        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()

        return user


# =========================================================
# VEHICLE FORM
# =========================================================

class VehicleForm(forms.ModelForm):

    class Meta:
        model = Vehicle

        fields = [
            "vehicle_number",
            "vehicle_type",
            "brand",
            "model",
            "year",
            "fuel_type",
        ]

        widgets = {

            "vehicle_number": forms.TextInput(
                attrs={
                    "placeholder": "KA01AB1234"
                }
            ),

            "vehicle_type": forms.Select(
                attrs={}
            ),

            "brand": forms.TextInput(
                attrs={
                    "placeholder": "Maruti, Hyundai, Tata..."
                }
            ),

            "model": forms.TextInput(
                attrs={
                    "placeholder": "Swift, Creta, Nexon..."
                }
            ),

            "year": forms.NumberInput(
                attrs={
                    "placeholder": "2024",
                    "min": "1900",
                    "max": "2100"
                }
            ),

            "fuel_type": forms.Select(
                attrs={}
            ),
        }


# =========================================================
# BOOKING FORM
# =========================================================

class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking

        fields = [
            "customer_name",
            "phone",

            "vehicle_type",
            "vehicle_number",
            "vehicle_brand",
            "vehicle_model",
            "vehicle_year",
            "fuel_type",

            "service",
            "booking_date",
            "notes",
        ]

        widgets = {

            # -------------------------------------------------
            # CUSTOMER
            # -------------------------------------------------

            "customer_name": forms.TextInput(
                attrs={
                    "placeholder": "Enter customer name",
                    "autocomplete": "name"
                }
            ),

            "phone": forms.TextInput(
                attrs={
                    "placeholder": "Enter phone number",
                    "autocomplete": "tel",
                    "maxlength": "20"
                }
            ),

            # -------------------------------------------------
            # VEHICLE
            # -------------------------------------------------

            "vehicle_type": forms.Select(
                attrs={}
            ),

            "vehicle_number": forms.TextInput(
                attrs={
                    "placeholder": "KA01AB1234",
                    "maxlength": "20"
                }
            ),

            "vehicle_brand": forms.TextInput(
                attrs={
                    "placeholder": "Hyundai, Tata, Maruti..."
                }
            ),

            "vehicle_model": forms.TextInput(
                attrs={
                    "placeholder": "Creta, Nexon, Swift..."
                }
            ),

            "vehicle_year": forms.NumberInput(
                attrs={
                    "placeholder": "2024",
                    "min": "1900",
                    "max": "2100"
                }
            ),

            "fuel_type": forms.Select(
                attrs={}
            ),

            # -------------------------------------------------
            # SERVICE
            # -------------------------------------------------

            "service": forms.Select(
                attrs={}
            ),

            # -------------------------------------------------
            # DATE & TIME
            # -------------------------------------------------

            "booking_date": forms.DateTimeInput(
                attrs={
                    "type": "datetime-local"
                }
            ),

            # -------------------------------------------------
            # NOTES
            # -------------------------------------------------

            "notes": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Any additional information..."
                }
            ),
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        # Only active services should be available
        # to customers for booking.

        self.fields["service"].queryset = (
            self.fields["service"].queryset
            .filter(is_active=True)
            .order_by("name")
        )

        # Better labels

        self.fields["customer_name"].label = "Customer Name"
        self.fields["phone"].label = "Phone Number"

        self.fields["vehicle_type"].label = "Vehicle Type"
        self.fields["vehicle_number"].label = "Vehicle Number"
        self.fields["vehicle_brand"].label = "Vehicle Brand"
        self.fields["vehicle_model"].label = "Vehicle Model"
        self.fields["vehicle_year"].label = "Vehicle Year"
        self.fields["fuel_type"].label = "Fuel Type"

        self.fields["service"].label = "Select Service"
        self.fields["booking_date"].label = "Preferred Date & Time"
        self.fields["notes"].label = "Additional Notes"


# =========================================================
# CONTACT FORM
# =========================================================

class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactMessage

        fields = [
            "name",
            "email",
            "phone",
            "subject",
            "message",
        ]

        widgets = {

            "name": forms.TextInput(
                attrs={
                    "placeholder": "Your name"
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Your email"
                }
            ),

            "phone": forms.TextInput(
                attrs={
                    "placeholder": "Phone number"
                }
            ),

            "subject": forms.TextInput(
                attrs={
                    "placeholder": "Subject"
                }
            ),

            "message": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "How can we help you?"
                }
            ),
        }
