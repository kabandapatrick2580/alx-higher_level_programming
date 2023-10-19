-- Import the database dump from hbtn_0d_tvshows
SELECT ts.title
FROM tv_shows ts
LEFT JOIN tv_genres tg ON ts.id = tg.show_id
WHERE tg.name IS NULL
ORDER BY ts.title ASC;
