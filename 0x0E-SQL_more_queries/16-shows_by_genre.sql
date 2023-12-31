-- SQL script that lists all shows, and all genres linked
-- to that show, from the database hbtn_0d_tvshows.
SELECT tv.title, g.name
	FROM tv_shows AS tv
	LEFT JOIN tv_show_genres AS tvg
	ON tvg.show_id = tv.id
	LEFT JOIN tv_genres AS g
	ON g.id = tvg.genre_id
	ORDER BY tv.title, g.name ASC;
