CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE gpx_route (
    id SERIAL PRIMARY KEY,
    location GEOMETRY(Point, 4326),
    distance DECIMAL
);

CREATE TEMP TABLE tmp_route (
    id SERIAL PRIMARY KEY,
    latitude DECIMAL,
    longitude DECIMAL,
    distance DECIMAL
);

COPY tmp_route(latitude, longitude, distance)
FROM '/data/gpx-route.csv'
DELIMITER ','
CSV HEADER;

INSERT INTO gpx_route (location, distance)
SELECT ST_SetSRID(ST_MakePoint(longitude, latitude), 4326), distance
FROM tmp_route;

DROP TABLE tmp_route;