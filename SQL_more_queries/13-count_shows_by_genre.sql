-- List all genres from hbtn_0d_tvshows and display the number of shows linked to each

SELECT
    genres.name AS genre,
    COUNT(tv_show_genres.show_id) AS number_of_shows
FROM
    genres
JOIN
    tv_show_genres
ON
    genres.id = tv_show_genres.genre_id
GROUP BY
    genres.id, genres.name
HAVING
    COUNT(tv_show_genres.show_id) > 0
ORDER BY
    number_of_shows DESC, genre ASC;

