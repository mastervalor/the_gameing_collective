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

    console.log("Upcoming", upcomingGames);
    console.log("Upcoming_games", upcoming_games);

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
    const actionContent = document.querySelector('.adventure_selection');
    const rpgContent = document.querySelector('.roleplaying_selection');
    const fightingContent = document.querySelector('.fighting_selection');
    const shooterContent = document.querySelector('.shooter_selection');
    const musicContent = document.querySelector('.music_selection');
    const platformContent = document.querySelector('.platform_selection');
    const puzzleContent = document.querySelector('.puzzle_selection');
    const racingContent = document.querySelector('.racing_selection');
    const rtsContent = document.querySelector('.rts_selection');
    const simContent = document.querySelector('.sim_selection');
    const sportContent = document.querySelector('.sport_selection');
    const defaultContent = document.querySelector('.default_selection');

    genreDropdown.addEventListener("change", function () {
        var selectedGenre = this.value;

        if (selectedGenre === 'adventure') {
            actionContent.classList.remove('hidden-content');
            rpgContent.classList.add('hidden-content');
            fightingContent.classList.add('hidden-content');
            shooterContent.classList.add('hidden-content');
            musicContent.classList.add('hidden-content');
            platformContent.classList.add('hidden-content');
            puzzleContent.classList.add('hidden-content');
            racingContent.classList.add('hidden-content');
            rtsContent.classList.add('hidden-content');
            simContent.classList.add('hidden-content');
            sportContent.classList.add('hidden-content');
            defaultContent.classList.add('hidden-content');
        }
        else if (selectedGenre === 'fighting') {
            fightingContent.classList.remove('hidden-content');
            actionContent.classList.add('hidden-content');
            rpgContent.classList.add('hidden-content');
            shooterContent.classList.add('hidden-content');
            musicContent.classList.add('hidden-content');
            platformContent.classList.add('hidden-content');
            puzzleContent.classList.add('hidden-content');
            racingContent.classList.add('hidden-content');
            rtsContent.classList.add('hidden-content');
            simContent.classList.add('hidden-content');
            sportContent.classList.add('hidden-content');
            defaultContent.classList.add('hidden-content');
        }
        else if (selectedGenre === 'rpg') {
            actionContent.classList.add('hidden-content');
            rpgContent.classList.remove('hidden-content');
            fightingContent.classList.add('hidden-content');
            shooterContent.classList.add('hidden-content');
            musicContent.classList.add('hidden-content');
            platformContent.classList.add('hidden-content');
            puzzleContent.classList.add('hidden-content');
            racingContent.classList.add('hidden-content');
            rtsContent.classList.add('hidden-content');
            simContent.classList.add('hidden-content');
            sportContent.classList.add('hidden-content');
            defaultContent.classList.add('hidden-content');
        }
        else if (selectedGenre === 'fighting') {
            actionContent.classList.add('hidden-content');
            rpgContent.classList.add('hidden-content');
            fightingContent.classList.remove('hidden-content');
            shooterContent.classList.add('hidden-content');
            musicContent.classList.add('hidden-content');
            platformContent.classList.add('hidden-content');
            puzzleContent.classList.add('hidden-content');
            racingContent.classList.add('hidden-content');
            rtsContent.classList.add('hidden-content');
            simContent.classList.add('hidden-content');
            sportContent.classList.add('hidden-content');
            defaultContent.classList.add('hidden-content');
        }
        else if (selectedGenre === 'shooter') {
            actionContent.classList.add('hidden-content');
            rpgContent.classList.add('hidden-content');
            fightingContent.classList.add('hidden-content');
            shooterContent.classList.remove('hidden-content');
            musicContent.classList.add('hidden-content');
            platformContent.classList.add('hidden-content');
            puzzleContent.classList.add('hidden-content');
            racingContent.classList.add('hidden-content');
            rtsContent.classList.add('hidden-content');
            simContent.classList.add('hidden-content');
            sportContent.classList.add('hidden-content');
            defaultContent.classList.add('hidden-content');
        }
        else if (selectedGenre === 'music') {
            actionContent.classList.add('hidden-content');
            rpgContent.classList.add('hidden-content');
            fightingContent.classList.add('hidden-content');
            shooterContent.classList.add('hidden-content');
            musicContent.classList.remove('hidden-content');
            platformContent.classList.add('hidden-content');
            puzzleContent.classList.add('hidden-content');
            racingContent.classList.add('hidden-content');
            rtsContent.classList.add('hidden-content');
            simContent.classList.add('hidden-content');
            sportContent.classList.add('hidden-content');
            defaultContent.classList.add('hidden-content');
        }
        else if (selectedGenre === 'platform') {
            actionContent.classList.add('hidden-content');
            rpgContent.classList.add('hidden-content');
            fightingContent.classList.add('hidden-content');
            shooterContent.classList.add('hidden-content');
            musicContent.classList.add('hidden-content');
            platformContent.classList.remove('hidden-content');
            puzzleContent.classList.add('hidden-content');
            racingContent.classList.add('hidden-content');
            rtsContent.classList.add('hidden-content');
            simContent.classList.add('hidden-content');
            sportContent.classList.add('hidden-content');
            defaultContent.classList.add('hidden-content');
        }
        else if (selectedGenre === 'puzzle') {
            actionContent.classList.add('hidden-content');
            rpgContent.classList.add('hidden-content');
            fightingContent.classList.add('hidden-content');
            shooterContent.classList.add('hidden-content');
            musicContent.classList.add('hidden-content');
            platformContent.classList.add('hidden-content');
            puzzleContent.classList.remove('hidden-content');
            racingContent.classList.add('hidden-content');
            rtsContent.classList.add('hidden-content');
            simContent.classList.add('hidden-content');
            sportContent.classList.add('hidden-content');
            defaultContent.classList.add('hidden-content');
        }
        else if (selectedGenre === 'racing') {
            actionContent.classList.add('hidden-content');
            rpgContent.classList.add('hidden-content');
            fightingContent.classList.add('hidden-content');
            shooterContent.classList.add('hidden-content');
            musicContent.classList.add('hidden-content');
            platformContent.classList.add('hidden-content');
            puzzleContent.classList.add('hidden-content');
            racingContent.classList.remove('hidden-content');
            rtsContent.classList.add('hidden-content');
            simContent.classList.add('hidden-content');
            sportContent.classList.add('hidden-content');
            defaultContent.classList.add('hidden-content');
        }
        else if (selectedGenre === 'rts') {
            actionContent.classList.add('hidden-content');
            rpgContent.classList.add('hidden-content');
            fightingContent.classList.add('hidden-content');
            shooterContent.classList.add('hidden-content');
            musicContent.classList.add('hidden-content');
            platformContent.classList.add('hidden-content');
            puzzleContent.classList.add('hidden-content');
            racingContent.classList.add('hidden-content');
            rtsContent.classList.remove('hidden-content');
            simContent.classList.add('hidden-content');
            sportContent.classList.add('hidden-content');
            defaultContent.classList.add('hidden-content');
        }
        else if (selectedGenre === 'simulator') {
            actionContent.classList.add('hidden-content');
            rpgContent.classList.add('hidden-content');
            fightingContent.classList.add('hidden-content');
            shooterContent.classList.add('hidden-content');
            musicContent.classList.add('hidden-content');
            platformContent.classList.add('hidden-content');
            puzzleContent.classList.add('hidden-content');
            racingContent.classList.add('hidden-content');
            rtsContent.classList.add('hidden-content');
            simContent.classList.remove('hidden-content');
            sportContent.classList.add('hidden-content');
            defaultContent.classList.add('hidden-content');
        }
        else if (selectedGenre === 'sport') {
            actionContent.classList.add('hidden-content');
            rpgContent.classList.add('hidden-content');
            fightingContent.classList.add('hidden-content');
            shooterContent.classList.add('hidden-content');
            musicContent.classList.add('hidden-content');
            platformContent.classList.add('hidden-content');
            puzzleContent.classList.add('hidden-content');
            racingContent.classList.add('hidden-content');
            rtsContent.classList.add('hidden-content');
            simContent.classList.add('hidden-content');
            sportContent.classList.remove('hidden-content');
            defaultContent.classList.add('hidden-content');
        }
        else {
            defaultContent.classList.remove('hidden-content');
            actionContent.classList.add('hidden-content');
            rpgContent.classList.add('hidden-content');
            fightingContent.classList.add('hidden-content');
            shooterContent.classList.add('hidden-content');
            musicContent.classList.add('hidden-content');
            platformContent.classList.add('hidden-content');
            puzzleContent.classList.add('hidden-content');
            racingContent.classList.add('hidden-content');
            rtsContent.classList.add('hidden-content');
            simContent.classList.add('hidden-content');
            sportContent.classList.add('hidden-content');
        }
    });
});
/* Filter Buttons */