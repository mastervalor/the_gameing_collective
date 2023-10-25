/* ------------------------------------Homepage Carousel------------------------------------- */
const myCarouselElement = document.querySelector('#carousel-indicators');

var carousel = new bootstrap.Carousel(myCarouselElement, {
    interval: 7000, // Set the desired interval in milliseconds (e.g., 3000 for 3 seconds)
    wrap: true, // Allow cycling from the last image to the first image
});

// Pause carousel on hover
document.getElementById('carousel-indicators').addEventListener('mouseenter', function () {
    carousel.pause();
});

// Resume carousel when not hovering
document.getElementById('carousel-indicators').addEventListener('mouseleave', function () {
    carousel.cycle();
});

var captionElement = document.querySelectorAll('.caption-text');
var maxLength = 50;

captionElement.forEach(function (captionElement) {
    var words = captionElement.textContent.split(' ');

    if (words.length > maxLength) {
        var truncatedText = words.slice(0, maxLength).join(' ') + '...';
        captionElement.textContent = truncatedText;
    }
});
/* ------------------------------------Homepage Carousel------------------------------------- */

/* --------------------------------Homepage Carousel Caption--------------------------------- */
document.addEventListener("DOMContentLoaded", function () {
    const releaseDateElements = document.querySelectorAll('.formatted-release-date');

    for (let i = 0; i < upcomingGames.length; i++) {
        const game = upcomingGames[i];
        const unixTimestamp = game.first_release_date;
        const releaseDate = new Date(unixTimestamp * 1000);

        const formattedDate = `${String(releaseDate.getDate()).padStart(2, '0')}/${String(releaseDate.getMonth() + 1).padStart(2, '0')}/${releaseDate.getFullYear()}`;

        // Use the index 'i' to select the correct release date element
        releaseDateElements[i].textContent = "Release Date: " + formattedDate;
    }
});
/* --------------------------------Homepage Carousel Caption--------------------------------- */