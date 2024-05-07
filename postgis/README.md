Run container:

```
docker run -p 5432:5432 evgenyarbatov/gpx-postgis:latest
```

Talk to DB:

```
psql -h localhost -U root -d gpx
```

Find the point closest to the given location (this gives distance):

```
SELECT id, location, distance, estimated_time
FROM gpx_route
ORDER BY location <-> ST_SetSRID(ST_MakePoint(103.89372498976476, 1.3095501745003915), 4326)
LIMIT 1;
```