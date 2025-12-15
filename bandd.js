// Simple availability check simulation
const availability = {
    "Sukhkarta Band": ["2025-12-05", "2025-12-10"],
    "Swarsamarat Band": ["2025-12-03", "2025-12-08"],
    "Nilkamal Band": ["2025-12-02", "2025-12-12"],
    "Devmamledar Band": ["2025-12-07", "2025-12-15"],
    "Rockstar Band": ["2025-12-01", "2025-12-09"]
};

function checkAvailability(band) {
    const today = new Date().toISOString().split('T')[0];
    if (availability[band].includes(today)) {
        alert(band + " is available today!");
    } else {
        alert(band + " is not available today.");
    }
}

// Booking form
document.getElementById('bookingForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const date = document.getElementById('date').value;
    const band = document.getElementById('band').value;

    if (availability[band].includes(date)) {
        document.getElementById('bookingMessage').innerText = `Sorry! ${band} is already booked on ${date}.`;
    } else {
        document.getElementById('bookingMessage').innerText = `Success! ${band} booked for ${date}.`;
        availability[band].push(date); // Add the booked date
    }
});
