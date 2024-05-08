CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE placemarks (
    id SERIAL PRIMARY KEY,
    location GEOMETRY(Point, 4326),
    name VARCHAR(255),
    distance DECIMAL
);

CREATE TEMP TABLE tmp_placemarks (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    latitude DECIMAL,
    longitude DECIMAL
);

COPY tmp_placemarks(name, latitude, longitude)
FROM '/data/placemarks.csv'
DELIMITER ','
CSV HEADER;

INSERT INTO placemarks (location, name)
SELECT ST_SetSRID(ST_MakePoint(longitude, latitude), 4326), name
FROM tmp_placemarks;

DROP TABLE tmp_placemarks;

WITH matched_routes AS (
    SELECT
        p.id AS placemark_id,
        r.distance AS distance,
        ROW_NUMBER() OVER (PARTITION BY p.id ORDER BY ST_Distance(p.location, r.location)) AS rn
    FROM
        placemarks p
    CROSS JOIN LATERAL
        (SELECT *
         FROM gpx_route
         ORDER BY p.location <-> location
         LIMIT 1) r
)
UPDATE placemarks
SET
    distance = m.distance
FROM
    matched_routes m
WHERE
    placemarks.id = m.placemark_id
    AND m.rn = 1;
