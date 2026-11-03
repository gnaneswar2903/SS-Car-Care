
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .models import (
    Service,
    SparePart,
    Vehicle,
    Booking,
    Order,
    ContactMessage,
)

from .forms import (
    RegisterForm,
    VehicleForm,
    BookingForm,
    ContactForm,
)


# =========================================================
# HOME
# =========================================================

def home(request):

    services = (
        Service.objects
        .filter(is_active=True)
        .order_by("name")
    )

    return render(
        request,
        "home/home.html",
        {
            "services": services,
        }
    )


# =========================================================
# CUSTOMER REGISTRATION
# =========================================================

def register_view(request):

    if request.user.is_authenticated:

        if request.user.is_staff:
            return redirect("owner_dashboard")

        return redirect("home")

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            messages.success(
                request,
                "Registration successful. Welcome to SS Car Care!"
            )

            return redirect("home")

    else:

        form = RegisterForm()

    return render(
        request,
        "home/register.html",
        {
            "form": form,
        }
    )


# =========================================================
# CUSTOMER LOGIN
# =========================================================

def login_view(request):

    if request.user.is_authenticated:

        if request.user.is_staff:
            return redirect("owner_dashboard")

        return redirect("home")

    if request.method == "POST":

        username = request.POST.get(
            "username",
            ""
        ).strip()

        password = request.POST.get(
            "password",
            ""
        )

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(
                request,
                user
            )

            if user.is_staff:
                return redirect("owner_dashboard")

            return redirect("home")

        messages.error(
            request,
            "Invalid username or password."
        )

    return render(
        request,
        "home/login.html"
    )


# =========================================================
# CUSTOMER LOGOUT
# =========================================================

def logout_view(request):

    logout(request)

    return redirect("home")


# =========================================================
# SERVICES
# =========================================================

def services(request):

    service_list = (
        Service.objects
        .filter(is_active=True)
        .order_by("name")
    )

    return render(
        request,
        "home/services.html",
        {
            "services": service_list,
        }
    )


# =========================================================
# SPARE PARTS
# =========================================================

def spare_parts(request):

    parts = (
        SparePart.objects
        .filter(is_active=True)
        .order_by("name")
    )

    return render(
        request,
        "home/spare_parts.html",
        {
            "spare_parts": parts,
        }
    )


# =========================================================
# BUY SPARE PART
# =========================================================

@login_required
def buy_part(request, part_id):

    if request.user.is_staff:

        messages.error(
            request,
            "Owner accounts cannot place customer orders."
        )

        return redirect("owner_dashboard")

    part = get_object_or_404(
        SparePart,
        id=part_id,
        is_active=True
    )

    if request.method == "POST":

        try:

            quantity = int(
                request.POST.get(
                    "quantity",
                    1
                )
            )

        except (TypeError, ValueError):

            quantity = 1

        if quantity < 1:
            quantity = 1

        if quantity > part.stock:

            messages.error(
                request,
                "Requested quantity is not available."
            )

            return redirect("spare_parts")

        vehicle_id = request.POST.get(
            "vehicle"
        )

        vehicle = None

        if vehicle_id:

            vehicle = get_object_or_404(
                Vehicle,
                id=vehicle_id,
                user=request.user
            )

        total_price = (
            part.price * quantity
        )

        Order.objects.create(

            user=request.user,

            spare_part=part,

            vehicle=vehicle,

            quantity=quantity,

            total_price=total_price,

            status="Placed"
        )

        messages.success(
            request,
            "Spare part order placed successfully."
        )

        return redirect("orders")

    return redirect("spare_parts")


# =========================================================
# ADD VEHICLE
# =========================================================

@login_required
def add_vehicle(request):

    if request.user.is_staff:

        messages.error(
            request,
            "Owner accounts cannot add customer vehicles."
        )

        return redirect("owner_dashboard")

    if request.method == "POST":

        form = VehicleForm(
            request.POST
        )

        if form.is_valid():

            vehicle = form.save(
                commit=False
            )

            vehicle.user = request.user

            vehicle.save()

            messages.success(
                request,
                "Vehicle added successfully."
            )

            return redirect("home")

    else:

        form = VehicleForm()

    return render(
        request,
        "home/add_vehicle.html",
        {
            "form": form,
        }
    )


# =========================================================
# DELETE VEHICLE
# =========================================================

@login_required
def delete_vehicle(
    request,
    vehicle_id
):

    if request.user.is_staff:

        messages.error(
            request,
            "Owner accounts cannot delete customer vehicles."
        )

        return redirect("owner_dashboard")

    vehicle = get_object_or_404(
        Vehicle,
        id=vehicle_id,
        user=request.user
    )

    vehicle.delete()

    messages.success(
        request,
        "Vehicle deleted successfully."
    )

    return redirect("home")


# =========================================================
# CUSTOMER SERVICE BOOKING
# =========================================================
#
# IMPORTANT:
# Customer does NOT need to login.
#
# Customer manually enters:
# - Name
# - Phone
# - Vehicle Type
# - Vehicle Number
# - Vehicle Brand
# - Vehicle Model
# - Vehicle Year
# - Fuel Type
# - Service
# - Date & Time
# - Notes
#
# Host can later see all these details.
# =========================================================

def book_service(request):

    if request.method != "POST":

        return redirect("home")

    # -----------------------------------------------------
    # CUSTOMER DETAILS
    # -----------------------------------------------------

    customer_name = request.POST.get(
        "customer_name",
        ""
    ).strip()

    phone = request.POST.get(
        "phone",
        ""
    ).strip()

    # -----------------------------------------------------
    # VEHICLE DETAILS
    # -----------------------------------------------------

    vehicle_type = request.POST.get(
        "vehicle_type",
        ""
    ).strip()

    vehicle_number = request.POST.get(
        "vehicle_number",
        ""
    ).strip()

    vehicle_brand = request.POST.get(
        "vehicle_brand",
        ""
    ).strip()

    vehicle_model = request.POST.get(
        "vehicle_model",
        ""
    ).strip()

    vehicle_year = request.POST.get(
        "vehicle_year",
        ""
    ).strip()

    fuel_type = request.POST.get(
        "fuel_type",
        ""
    ).strip()

    # -----------------------------------------------------
    # SERVICE DETAILS
    # -----------------------------------------------------

    service_id = request.POST.get(
        "service"
    )

    booking_date = request.POST.get(
        "booking_date"
    )

    notes = request.POST.get(
        "notes",
        ""
    ).strip()

    # =====================================================
    # VALIDATION
    # =====================================================

    if not customer_name:

        messages.error(
            request,
            "Please enter the customer name."
        )

        return redirect("home")

    if not phone:

        messages.error(
            request,
            "Please enter the customer phone number."
        )

        return redirect("home")

    if not vehicle_type:

        messages.error(
            request,
            "Please select the vehicle type."
        )

        return redirect("home")

    if not vehicle_number:

        messages.error(
            request,
            "Please enter the vehicle number."
        )

        return redirect("home")

    if not vehicle_brand:

        messages.error(
            request,
            "Please enter the vehicle brand."
        )

        return redirect("home")

    if not vehicle_model:

        messages.error(
            request,
            "Please enter the vehicle model."
        )

        return redirect("home")

    if not service_id:

        messages.error(
            request,
            "Please select a service."
        )

        return redirect("home")

    if not booking_date:

        messages.error(
            request,
            "Please select a booking date and time."
        )

        return redirect("home")

    # =====================================================
    # GET SERVICE
    # =====================================================

    service = get_object_or_404(
        Service,
        id=service_id,
        is_active=True
    )

    # =====================================================
    # VEHICLE YEAR
    # =====================================================

    if vehicle_year:

        try:

            vehicle_year = int(
                vehicle_year
            )

        except ValueError:

            messages.error(
                request,
                "Please enter a valid vehicle year."
            )

            return redirect("home")

    else:

        vehicle_year = None

    # =====================================================
    # CREATE BOOKING
    # =====================================================

    booking = Booking.objects.create(

        # Customer
        customer_name=customer_name,

        phone=phone,

        # Vehicle
        vehicle_type=vehicle_type,

        vehicle_number=vehicle_number,

        vehicle_brand=vehicle_brand,

        vehicle_model=vehicle_model,

        vehicle_year=vehicle_year,

        fuel_type=fuel_type,

        # Service
        service=service,

        booking_date=booking_date,

        # Price automatically comes
        # from the selected service
        amount=service.price,

        # Status
        status="Booked",

        payment_status="Pending",

        notes=notes,
    )

    # =====================================================
    # STORE BOOKING IN SESSION
    # =====================================================
    #
    # Customer can view/track their own bookings
    # from the same browser without creating an account.
    # =====================================================

    booking_ids = request.session.get(
        "booking_ids",
        []
    )

    if booking.id not in booking_ids:

        booking_ids.append(
            booking.id
        )

    request.session["booking_ids"] = booking_ids

    request.session["latest_booking_id"] = booking.id

    # =====================================================
    # SUCCESS MESSAGE
    # =====================================================

    messages.success(
        request,
        f"Booking #{booking.id} confirmed successfully!"
    )

    # Reload services so the same homepage design
    # continues to work.

    services = (
        Service.objects
        .filter(is_active=True)
        .order_by("name")
    )

    return render(
        request,
        "home/home.html",
        {
            "services": services,
            "booking_success": booking,
        }
    )


# =========================================================
# CUSTOMER BOOKINGS
# =========================================================

def bookings(request):

    booking_ids = request.session.get(
        "booking_ids",
        []
    )

    booking_list = (
        Booking.objects
        .filter(
            id__in=booking_ids
        )
        .select_related("service")
        .order_by("-booking_date")
    )

    return render(
        request,
        "home/bookings.html",
        {
            "bookings": booking_list,
        }
    )


# =========================================================
# CANCEL BOOKING
# =========================================================

def cancel_booking(
    request,
    booking_id
):

    booking_ids = request.session.get(
        "booking_ids",
        []
    )

    booking = get_object_or_404(
        Booking,
        id=booking_id,
        id__in=booking_ids
    )

    if booking.status not in [
        "Completed",
        "Cancelled"
    ]:

        booking.status = "Cancelled"

        booking.save()

        messages.success(
            request,
            f"Booking #{booking.id} cancelled successfully."
        )

    return redirect("bookings")


# =========================================================
# TRACK SERVICE
# =========================================================

def track_service(request):

    booking = None

    booking_id = request.GET.get(
        "booking_id"
    )

    booking_ids = request.session.get(
        "booking_ids",
        []
    )

    if booking_id:

        try:

            booking_id = int(
                booking_id
            )

        except (TypeError, ValueError):

            booking_id = None

        if booking_id:

            if booking_id in booking_ids:

                try:

                    booking = (
                        Booking.objects
                        .select_related("service")
                        .get(
                            id=booking_id
                        )
                    )

                except Booking.DoesNotExist:

                    messages.error(
                        request,
                        "Booking not found."
                    )

            else:

                messages.error(
                    request,
                    "You can only track bookings created from this browser."
                )

    return render(
        request,
        "home/track_service.html",
        {
            "tracking_booking": booking,
        }
    )


# =========================================================
# CUSTOMER ORDERS
# =========================================================

@login_required
def orders(request):

    if request.user.is_staff:

        return redirect(
            "owner_dashboard"
        )

    order_list = (
        Order.objects
        .filter(
            user=request.user
        )
        .select_related(
            "spare_part",
            "vehicle"
        )
        .order_by("-created_at")
    )

    return render(
        request,
        "home/orders.html",
        {
            "orders": order_list,
        }
    )


# =========================================================
# CONTACT
# =========================================================

def contact(request):

    if request.method == "POST":

        form = ContactForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Your message has been sent successfully."
            )

            return redirect("home")

    else:

        form = ContactForm()

    return render(
        request,
        "home/contact.html",
        {
            "form": form,
        }
    )


# =========================================================
# OWNER LOGIN
# =========================================================

def owner_login(request):

    if (
        request.user.is_authenticated
        and request.user.is_staff
    ):

        return redirect(
            "owner_dashboard"
        )

    if request.method == "POST":

        username = request.POST.get(
            "username",
            ""
        ).strip()

        password = request.POST.get(
            "password",
            ""
        )

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            if user.is_staff:

                login(
                    request,
                    user
                )

                return redirect(
                    "owner_dashboard"
                )

            messages.error(
                request,
                "You do not have owner access."
            )

        else:

            messages.error(
                request,
                "Invalid username or password."
            )

    return render(
        request,
        "home/owner_login.html"
    )


# =========================================================
# OWNER DASHBOARD
# =========================================================

@login_required
def owner_dashboard(request):

    if not request.user.is_staff:

        return redirect("home")

    # -----------------------------------------------------
    # CUSTOMER COUNT
    # -----------------------------------------------------

    customer_phones = (
        Booking.objects
        .exclude(phone="")
        .values_list(
            "phone",
            flat=True
        )
        .distinct()
    )

    total_customers = len(
        list(customer_phones)
    )

    # -----------------------------------------------------
    # COUNTERS
    # -----------------------------------------------------

    total_cars = Vehicle.objects.count()

    total_bookings = Booking.objects.count()

    pending_bookings = (
        Booking.objects
        .filter(
            status__in=[
                "Booked",
                "Confirmed"
            ]
        )
        .count()
    )

    completed_bookings = (
        Booking.objects
        .filter(
            status="Completed"
        )
        .count()
    )

    total_orders = Order.objects.count()

    # -----------------------------------------------------
    # RECENT BOOKINGS
    # -----------------------------------------------------

    recent_bookings = (
        Booking.objects
        .select_related("service")
        .order_by("-created_at")[:10]
    )

    context = {

        "total_customers":
            total_customers,

        "total_cars":
            total_cars,

        "total_bookings":
            total_bookings,

        "pending_bookings":
            pending_bookings,

        "completed_bookings":
            completed_bookings,

        "total_orders":
            total_orders,

        "recent_bookings":
            recent_bookings,
    }

    return render(
        request,
        "home/owner_dashboard.html",
        context
    )


# =========================================================
# OWNER BOOKINGS
# =========================================================

@login_required
def owner_bookings(request):

    if not request.user.is_staff:

        return redirect("home")

    booking_list = (
        Booking.objects
        .select_related("service")
        .order_by("-created_at")
    )

    return render(
        request,
        "home/owner_bookings.html",
        {
            "bookings": booking_list,
        }
    )


# =========================================================
# OWNER UPDATE BOOKING
# =========================================================

@login_required
def owner_update_booking(
    request,
    booking_id
):

    if not request.user.is_staff:

        return redirect("home")

    booking = get_object_or_404(
        Booking,
        id=booking_id
    )

    if request.method == "POST":

        new_status = request.POST.get(
            "status"
        )

        valid_statuses = [
            choice[0]
            for choice in Booking.STATUS_CHOICES
        ]

        if new_status in valid_statuses:

            booking.status = new_status

            booking.save()

            messages.success(
                request,
                f"Booking #{booking.id} status updated."
            )

    return redirect(
        "owner_bookings"
    )


# =========================================================
# OWNER CARS
# =========================================================

@login_required
def owner_cars(request):

    if not request.user.is_staff:

        return redirect("home")

    cars = (
        Vehicle.objects
        .select_related("user")
        .order_by("-created_at")
    )

    return render(
        request,
        "home/owner_cars.html",
        {
            "cars": cars,
        }
    )


# =========================================================
# OWNER SERVICES
# =========================================================

@login_required
def owner_services(request):

    if not request.user.is_staff:

        return redirect("home")

    service_list = (
        Service.objects
        .all()
        .order_by("name")
    )

    return render(
        request,
        "home/owner_services.html",
        {
            "services": service_list,
        }
    )


# =========================================================
# OWNER ORDERS
# =========================================================

@login_required
def owner_orders(request):

    if not request.user.is_staff:

        return redirect("home")

    order_list = (
        Order.objects
        .select_related(
            "user",
            "vehicle",
            "spare_part"
        )
        .order_by("-created_at")
    )

    return render(
        request,
        "home/owner_orders.html",
        {
            "orders": order_list,
        }
    )


# =========================================================
# OWNER CUSTOMERS
# =========================================================

@login_required
def owner_customers(request):

    if not request.user.is_staff:

        return redirect("home")

    customers = (
        Booking.objects
        .exclude(customer_name="")
        .select_related("service")
        .order_by("-created_at")
    )

    return render(
        request,
        "home/owner_customers.html",
        {
            "customers": customers,
        }
    )


# =========================================================
# OWNER MESSAGES
# =========================================================

@login_required
def owner_messages(request):

    if not request.user.is_staff:

        return redirect("home")

    contact_messages = (
        ContactMessage.objects
        .all()
        .order_by("-created_at")
    )

    return render(
        request,
        "home/owner_messages.html",
        {
            "messages_list":
                contact_messages,
        }
    )


# =========================================================
# OWNER LOGOUT
# =========================================================

@login_required
def owner_logout(request):

    if not request.user.is_staff:

        logout(request)

        return redirect("home")

    logout(request)

    return redirect("owner_login")
