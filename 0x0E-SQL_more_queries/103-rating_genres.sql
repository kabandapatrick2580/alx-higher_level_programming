-- Import the database dump from hbtn_0d_tvshows_rate
SELECT tg.name AS genre_name, SUM(tgr.rating) AS rating_sum
FROM tv_genres tg
LEFT JOIN tv_shows_genres tsg ON tg.id = tsg.genre_id
LEFT JOIN hbtn_0d_tvshows_rate tgr ON tsg.show_id = tgr.show_id
GROUP BY tg.name
ORDER BY rating_sum DESC;
