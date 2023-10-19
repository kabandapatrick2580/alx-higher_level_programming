-- Import the database hbtn_0d_tvshows_rate
SELECT title, SUM(rating) AS rating_sum
FROM hbtn_0d_tvshows_rate
GROUP BY title
ORDER BY rating_sum DESC;
