-- the same as the previous one
SELECT tv_genres.name
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.tv_show_id = tv_shows.id AND tv_shows.title = 'Dexter'
WHERE tv_shows.id IS NULL
ORDER BY tv_genres.name ASC;
