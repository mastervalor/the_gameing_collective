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
    const platformElements = document.querySelectorAll('.platforms');

    for (let i = 0; i < releaseDateElements.length; i++) {
        const releaseDateElement = releaseDateElements[i];
        const game = upcomingGames[i];

        if (game) {
            const unixTimestamp = game.first_release_date;
            const releaseDate = new Date(unixTimestamp * 1000);
            const formattedDate = `${String(releaseDate.getDate()).padStart(2, '0')}/${String(releaseDate.getMonth() + 1).padStart(2, '0')}/${releaseDate.getFullYear()}`;

            // Use the index 'i' to select the correct release date element
            releaseDateElement.textContent = "Release Date: " + formattedDate;
        }

        const platforms = game.platforms.map(platform => platform.name).join(', ');

        platformElements[i].textContent = "Platforms: " + platforms;
    }
});
/* --------------------------------Homepage Carousel Caption--------------------------------- */

/* -------------------------------------NAV bar---------------------------------------------- */
$(document).ready(function () {
    $(".navbar-toggler").click(function () {
        $(".sidebar").toggleClass("collapsed");
    });
});
/* ------------------------------------NAV bar----------------------------------------------- */

/* Filter Buttons */
document.addEventListener("DOMContentLoaded", function () {
    const genreDropdown = document.getElementById("genre-select");
    const actionContent = document.querySelector('.action_selection');

    genreDropdown.addEventListener("change", function () {
        var selectedGenre = this.value;

        if (selectedGenre === 'action') {
            actionContent.classList.remove('hidden-content');
        }
        else {
            actionContent.classList.add('hidden-content');
        }
    });
});
/* Filter Buttons */