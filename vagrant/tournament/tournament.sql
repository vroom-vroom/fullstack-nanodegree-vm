-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


CREATE TABLE players (id serial PRIMARY KEY, name text);
CREATE TABLE matches (id serial PRIMARY KEY, winner integer REFERENCES players(id), looser integer REFERENCES players(id));

CREATE VIEW standings AS
SELECT
    p.id,
    p.name,
    COUNT(DISTINCT m1.id) as wins,
    COUNT(DISTINCT m1.id) + COUNT(DISTINCT m2.id) as matches 
FROM
    players p
    LEFT JOIN matches as m1 ON p.id = m1.winner
    LEFT JOIN matches as m2 ON p.id = m2.looser
GROUP BY p.id
ORDER BY wins DESC;