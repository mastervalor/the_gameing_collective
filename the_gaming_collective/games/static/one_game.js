/* Single Game Data */
document.addEventListener("DOMContentLoaded", function () {
    // Since single_game is an array with one object, access the first object directly
    const game = singleGame[0];
    console.log("Game data:", game);
    console.log("Value: ", game.involved_companies[0].developer);

    // Assuming there's always at least one game object in the array
    if (game) {
        // Handle release date
        if (game.first_release_date) {
            const releaseDateElement = document.querySelector('.single_formatted_release_date');
            const unixTimestamp = game.first_release_date;
            const releaseDate = new Date(unixTimestamp * 1000);
            const formattedDate = `${String(releaseDate.getDate()).padStart(2, '0')}/${String(releaseDate.getMonth() + 1).padStart(2, '0')}/${releaseDate.getFullYear()}`;
            releaseDateElement.textContent = "Release Date: " + formattedDate;
        }

        // Handle platforms
        if (game.platforms && game.platforms.length > 0) {
            const platformElement = document.querySelector('.single_platforms');
            const platforms = game.platforms.map(platform => platform.name).join(', ');
            platformElement.textContent = "Platforms: " + platforms;
        }

        if (game.genres && game.genres.length > 0) {
            const genreElements = document.querySelector('.single_genres');
            const genres = game.genres.map(genre => genre.name).join(', ');
            genreElements.textContent = "Genres: " + genres;
        }

        
    }
});
/* Single Game Data */