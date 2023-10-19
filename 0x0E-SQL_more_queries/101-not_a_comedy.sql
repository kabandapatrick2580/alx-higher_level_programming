-- this script to to list all shows without genre comedy
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.id NOT IN (
    SELECT tv_shows.id
    FROM tv_shows
    JOIN tv_shows_genres ON tv_shows.id = tv_shows_genres.show_id
    JOIN tv_genres ON tv_shows_genres.genre_id = tv_genres.id
    WHERE tv_genres.name = 'Comedy'
)
ORDER BY tv_shows.title ASC;
