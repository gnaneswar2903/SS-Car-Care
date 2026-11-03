/* =========================================================
   SS CAR CARE
   FRONTEND JAVASCRIPT
   ========================================================= */


/* =========================================================
   MOBILE NAVIGATION
   ========================================================= */

const mobileMenuButton =
    document.getElementById("mobileMenuButton");

const mobileNav =
    document.getElementById("mobileNav");


if (mobileMenuButton && mobileNav) {

    mobileMenuButton.addEventListener("click", function () {

        mobileNav.classList.toggle("open");

    });


    const mobileLinks =
        mobileNav.querySelectorAll("a");


    mobileLinks.forEach(function (link) {

        link.addEventListener("click", function () {

            mobileNav.classList.remove("open");

        });

    });

}



/* =========================================================
   SET MINIMUM BOOKING DATE
   ========================================================= */

const serviceDate =
    document.getElementById("serviceDate");


if (serviceDate) {

    const today =
        new Date().toISOString().split("T")[0];

    serviceDate.setAttribute(
        "min",
        today
    );

}



/* =========================================================
   BOOKING FORM
   ========================================================= */

const bookingForm =
    document.getElementById("bookingForm");


const bookingModal =
    document.getElementById("bookingModal");


const generatedServiceId =
    document.getElementById("generatedServiceId");


if (bookingForm) {

    bookingForm.addEventListener(
        "submit",
        function (event) {

            event.preventDefault();


            /*
             * Generate a simple frontend
             * service ID.
             */

            const randomNumber =
                Math.floor(
                    1000 + Math.random() * 9000
                );


            const serviceId =
                "SSC" + randomNumber;


            if (generatedServiceId) {

                generatedServiceId.textContent =
                    serviceId;

            }


            /*
             * Save booking information
             * locally for prototype purposes.
             */

            const bookingData = {

                id: serviceId,

                name:
                    document.getElementById(
                        "customerName"
                    ).value,

                phone:
                    document.getElementById(
                        "customerPhone"
                    ).value,

                service:
                    document.getElementById(
                        "service"
                    ).value,

                vehicle:
                    document.getElementById(
                        "vehicleType"
                    ).value,

                date:
                    document.getElementById(
                        "serviceDate"
                    ).value,

                time:
                    document.getElementById(
                        "serviceTime"
                    ).value,

                additionalInfo:
                    document.getElementById(
                        "additionalInfo"
                    ).value,

                status:
                    "Booking Confirmed"

            };


            localStorage.setItem(
                serviceId,
                JSON.stringify(bookingData)
            );


            /*
             * Show confirmation modal.
             */

            if (bookingModal) {

                bookingModal.classList.add(
                    "show"
                );

            }

        }
    );

}



/* =========================================================
   CLOSE BOOKING MODAL
   ========================================================= */

const modalClose =
    document.getElementById("modalClose");


const modalDone =
    document.getElementById("modalDone");


function closeBookingModal() {

    if (bookingModal) {

        bookingModal.classList.remove(
            "show"
        );

    }


    if (bookingForm) {

        bookingForm.reset();

    }

}


if (modalClose) {

    modalClose.addEventListener(
        "click",
        closeBookingModal
    );

}


if (modalDone) {

    modalDone.addEventListener(
        "click",
        closeBookingModal
    );

}


if (bookingModal) {

    bookingModal.addEventListener(
        "click",
        function (event) {

            if (
                event.target === bookingModal
            ) {

                closeBookingModal();

            }

        }
    );

}



/* =========================================================
   SERVICE TRACKING
   ========================================================= */

const trackingForm =
    document.getElementById("trackingForm");


const trackingResult =
    document.getElementById("trackingResult");


if (trackingForm) {

    trackingForm.addEventListener(
        "submit",
        function (event) {

            event.preventDefault();


            const trackingId =
                document.getElementById(
                    "trackingId"
                ).value
                .trim()
                .toUpperCase();


            if (!trackingId) {

                return;

            }


            /*
             * Check locally stored booking.
             */

            const savedBooking =
                localStorage.getItem(
                    trackingId
                );


            if (savedBooking) {

                const booking =
                    JSON.parse(
                        savedBooking
                    );


                showTrackingResult(
                    booking
                );


                return;

            }


            /*
             * Demo service IDs.
             */

            const demoBookings = {

                SSC1001: {

                    id: "SSC1001",

                    name: "Demo Customer",

                    service:
                        "Full Car Detailing",

                    vehicle:
                        "Sedan",

                    status:
                        "Vehicle Under Service"

                },


                SSC1002: {

                    id: "SSC1002",

                    name: "Demo Customer",

                    service:
                        "Interior Cleaning",

                    vehicle:
                        "SUV",

                    status:
                        "Service Completed"

                },


                SSC1003: {

                    id: "SSC1003",

                    name: "Demo Customer",

                    service:
                        "Exterior Detailing",

                    vehicle:
                        "Hatchback",

                    status:
                        "Service Confirmed"

                }

            };


            if (
                demoBookings[trackingId]
            ) {

                showTrackingResult(
                    demoBookings[trackingId]
                );

            } else {

                trackingResult.innerHTML = `

                    <div class="tracking-error">

                        <strong>
                            Service ID Not Found
                        </strong>

                        <p>
                            Please check the service ID
                            and try again.
                        </p>

                    </div>

                `;

            }

        }
    );

}



/* =========================================================
   TRACKING RESULT
   ========================================================= */

function showTrackingResult(booking) {

    if (!trackingResult) {

        return;

    }


    trackingResult.innerHTML = `

        <div class="tracking-card">

            <div class="tracking-card-header">

                <div>

                    <span>
                        SERVICE ID
                    </span>

                    <strong>
                        ${booking.id}
                    </strong>

                </div>


                <div class="tracking-status">

                    ${booking.status}

                </div>

            </div>


            <div class="tracking-details">

                <div>

                    <span>Service</span>

                    <strong>
                        ${booking.service}
                    </strong>

                </div>


                <div>

                    <span>Vehicle</span>

                    <strong>
                        ${booking.vehicle}
                    </strong>

                </div>

            </div>


            <div class="tracking-timeline">

                <div class="timeline-item completed">

                    <div class="timeline-dot"></div>

                    <div>

                        <strong>
                            Booking Confirmed
                        </strong>

                        <span>
                            Your service request has been received.
                        </span>

                    </div>

                </div>


                <div class="timeline-item completed">

                    <div class="timeline-dot"></div>

                    <div>

                        <strong>
                            Vehicle Received
                        </strong>

                        <span>
                            Vehicle checked in for service.
                        </span>

                    </div>

                </div>


                <div class="timeline-item active">

                    <div class="timeline-dot"></div>

                    <div>

                        <strong>
                            ${booking.status}
                        </strong>

                        <span>
                            Our team is currently processing your service.
                        </span>

                    </div>

                </div>


                <div class="timeline-item">

                    <div class="timeline-dot"></div>

                    <div>

                        <strong>
                            Ready for Collection
                        </strong>

                        <span>
                            You will be notified when your vehicle is ready.
                        </span>

                    </div>

                </div>

            </div>

        </div>

    `;

}



/* =========================================================
   CLOSE TRACKING RESULT WHEN USER CHANGES ID
   ========================================================= */

const trackingInput =
    document.getElementById("trackingId");


if (trackingInput) {

    trackingInput.addEventListener(
        "input",
        function () {

            if (trackingResult) {

                trackingResult.innerHTML = "";

            }

        }
    );

}



/* =========================================================
   SMOOTH SCROLL
   ========================================================= */

const allAnchorLinks =
    document.querySelectorAll(
        'a[href^="#"]'
    );


allAnchorLinks.forEach(function (link) {

    link.addEventListener(
        "click",
        function (event) {

            const targetId =
                this.getAttribute("href");


            if (
                targetId === "#" ||
                !targetId
            ) {

                return;

            }


            const target =
                document.querySelector(
                    targetId
                );


            if (target) {

                event.preventDefault();


                target.scrollIntoView({

                    behavior: "smooth",

                    block: "start"

                });

            }

        }
    );

});