$(document).ready(function() {
	$.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
		const cinemas = data.results;
		const liste = $('#list_movies');

		$.each(cinemas, function(index, movie) {
			liste.append($('<li>').text(movie.title));
		});
	});
});
