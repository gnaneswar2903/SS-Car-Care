/* =========================================================
   SS CAR CARE - MAIN JAVASCRIPT
========================================================= */

document.addEventListener("DOMContentLoaded", function () {


    /* =====================================================
       MOBILE MENU
    ===================================================== */

    const menuButton =
        document.querySelector(".mobile-menu-button");

    const mobileMenu =
        document.querySelector(".mobile-nav");

    if (menuButton && mobileMenu) {

        menuButton.addEventListener(
            "click",
            function () {

                mobileMenu.classList.toggle("active");

            }
        );

    }


    /* =====================================================
       CLOSE MOBILE MENU AFTER CLICK
    ===================================================== */

    const mobileLinks =
        document.querySelectorAll(".mobile-nav a");

    mobileLinks.forEach(function (link) {

        link.addEventListener(
            "click",
            function () {

                if (mobileMenu) {
                    mobileMenu.classList.remove("active");
                }

            }
        );

    });


    /* =====================================================
       BOOKING SERVICE DETAILS
    ===================================================== */

    const serviceSelect =
        document.getElementById("service");

    const serviceInfo =
        document.getElementById(
            "selectedServiceInfo"
        );

    const serviceName =
        document.getElementById(
            "selectedServiceName"
        );

    const servicePrice =
        document.getElementById(
            "selectedServicePrice"
        );

    const serviceDuration =
        document.getElementById(
            "selectedServiceDuration"
        );


    if (
        serviceSelect &&
        serviceInfo &&
        serviceName &&
        servicePrice &&
        serviceDuration
    ) {

        serviceSelect.addEventListener(
            "change",
            function () {

                const selectedOption =
                    serviceSelect.options[
                        serviceSelect.selectedIndex
                    ];


                if (
                    !selectedOption ||
                    !selectedOption.value
                ) {

                    serviceInfo.style.display =
                        "none";

                    return;

                }


                const name =
                    selectedOption.textContent
                        .split("—")[0]
                        .trim();


                const price =
                    selectedOption.dataset.price;


                const duration =
                    selectedOption.dataset.duration;


                serviceName.textContent =
                    name || "—";


                if (price) {

                    servicePrice.textContent =
                        "₹" + price;

                } else {

                    servicePrice.textContent =
                        "Contact us";

                }


                if (duration) {

                    serviceDuration.textContent =
                        duration;

                } else {

                    serviceDuration.textContent =
                        "As required";

                }


                serviceInfo.style.display =
                    "grid";

            }
        );

    }


    /* =====================================================
       BOOKING DATE - MINIMUM CURRENT DATE/TIME
    ===================================================== */

    const bookingDate =
        document.getElementById(
            "bookingDate"
        );


    if (bookingDate) {

        const now =
            new Date();


        const year =
            now.getFullYear();


        const month =
            String(
                now.getMonth() + 1
            ).padStart(2, "0");


        const day =
            String(
                now.getDate()
            ).padStart(2, "0");


        const hours =
            String(
                now.getHours()
            ).padStart(2, "0");


        const minutes =
            String(
                now.getMinutes()
            ).padStart(2, "0");


        bookingDate.min =
            `${year}-${month}-${day}T${hours}:${minutes}`;

    }


    /* =====================================================
       BOOKING SUCCESS MODAL
    ===================================================== */

    window.closeBookingSuccess =
        function () {

            const modal =
                document.getElementById(
                    "bookingSuccessModal"
                );


            if (modal) {

                modal.style.display =
                    "none";

            }

        };


    /* =====================================================
       ESC KEY CLOSE SUCCESS POPUP
    ===================================================== */

    document.addEventListener(
        "keydown",
        function (event) {

            if (event.key === "Escape") {

                const modal =
                    document.getElementById(
                        "bookingSuccessModal"
                    );


                if (modal) {

                    modal.style.display =
                        "none";

                }

            }

        }
    );

});