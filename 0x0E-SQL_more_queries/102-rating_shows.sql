-- this is aonther one of the advanced
SELECT tv_shows.title, SUM(hbtn_0d_tvshows_rate.rating) AS rating_sum
FROM tv_shows
LEFT JOIN hbtn_0d_tvshows_rate ON tv_shows.id = hbtn_0d_tvshows_rate.show_id
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;
