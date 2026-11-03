from django.urls import path

from . import views


urlpatterns = [

    # =====================================================
    # CUSTOMER WEBSITE
    # =====================================================

    path(
        "",
        views.home,
        name="home"
    ),

    path(
        "register/",
        views.register_view,
        name="register"
    ),

    path(
        "login/",
        views.login_view,
        name="login"
    ),

    path(
        "logout/",
        views.logout_view,
        name="logout"
    ),


    # =====================================================
    # SERVICES
    # =====================================================

    path(
        "services/",
        views.services,
        name="services"
    ),


    # =====================================================
    # SPARE PARTS
    # =====================================================

    path(
        "spare-parts/",
        views.spare_parts,
        name="spare_parts"
    ),

    path(
        "spare-parts/buy/<int:part_id>/",
        views.buy_part,
        name="buy_part"
    ),


    # =====================================================
    # VEHICLES
    # =====================================================

    path(
        "vehicles/add/",
        views.add_vehicle,
        name="add_vehicle"
    ),

    path(
        "vehicles/delete/<int:vehicle_id>/",
        views.delete_vehicle,
        name="delete_vehicle"
    ),


    # =====================================================
    # SERVICE BOOKING
    # =====================================================

    path(
        "booking/",
        views.book_service,
        name="booking"
    ),

    path(
        "bookings/",
        views.bookings,
        name="bookings"
    ),

    path(
        "booking/cancel/<int:booking_id>/",
        views.cancel_booking,
        name="cancel_booking"
    ),


    # =====================================================
    # SERVICE TRACKING
    # =====================================================

    path(
        "track-service/",
        views.track_service,
        name="track_service"
    ),


    # =====================================================
    # ORDERS
    # =====================================================

    path(
        "orders/",
        views.orders,
        name="orders"
    ),


    # =====================================================
    # CONTACT
    # =====================================================

    path(
        "contact/",
        views.contact,
        name="contact"
    ),


    # =====================================================
    # OWNER LOGIN
    # =====================================================

    path(
        "owner-login/",
        views.owner_login,
        name="owner_login"
    ),


    # =====================================================
    # OWNER DASHBOARD
    # =====================================================

    path(
        "owner-dashboard/",
        views.owner_dashboard,
        name="owner_dashboard"
    ),


    # =====================================================
    # OWNER BOOKINGS
    # =====================================================

    path(
        "owner/bookings/",
        views.owner_bookings,
        name="owner_bookings"
    ),

    path(
        "owner/bookings/<int:booking_id>/update/",
        views.owner_update_booking,
        name="owner_update_booking"
    ),


    # =====================================================
    # OWNER CARS
    # =====================================================

    path(
        "owner/cars/",
        views.owner_cars,
        name="owner_cars"
    ),


    # =====================================================
    # OWNER SERVICES
    # =====================================================

    path(
        "owner/services/",
        views.owner_services,
        name="owner_services"
    ),


    # =====================================================
    # OWNER ORDERS
    # =====================================================

    path(
        "owner/orders/",
        views.owner_orders,
        name="owner_orders"
    ),


    # =====================================================
    # OWNER CUSTOMERS
    # =====================================================

    path(
        "owner/customers/",
        views.owner_customers,
        name="owner_customers"
    ),


    # =====================================================
    # OWNER MESSAGES
    # =====================================================

    path(
        "owner/messages/",
        views.owner_messages,
        name="owner_messages"
    ),


    # =====================================================
    # OWNER LOGOUT
    # =====================================================

    path(
        "owner-logout/",
        views.owner_logout,
        name="owner_logout"
    ),

]