CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE gpx_route (
    id SERIAL PRIMARY KEY,
    location GEOMETRY(Point, 4326),
    distance DECIMAL,
    cutoff_time VARCHAR(255),
    street VARCHAR(255),
    planned_hours DECIMAL,
    planned_time VARCHAR(255)
);

CREATE TEMP TABLE tmp_route (
    id SERIAL PRIMARY KEY,
    latitude DECIMAL,
    longitude DECIMAL,
    distance DECIMAL,
    cutoff_time VARCHAR(255),
    street VARCHAR(255),
    planned_hours DECIMAL,
    planned_time VARCHAR(255)
);

COPY tmp_route(
    latitude, 
    longitude, 
    distance, 
    cutoff_time, 
    street, 
    planned_hours, 
    planned_time
)
FROM '/data/gpx-route.csv'
DELIMITER ','
CSV HEADER;

INSERT INTO gpx_route (
    location, 
    distance, 
    cutoff_time, 
    street, 
    planned_hours, 
    planned_time
)
SELECT 
    ST_SetSRID(ST_MakePoint(longitude, latitude), 4326), 
    distance, 
    cutoff_time, 
    street, 
    planned_hours, 
    planned_time
FROM tmp_route;

DROP TABLE tmp_route;