Precompute reverse geocoding queries so we do not have to do this on the fly:

- Download OSM extract from [here](https://download.openstreetmap.fr/extracts/asia/)
- Run [Nominatim](https://github.com/mediagis/nominatim-docker/tree/master/4.4) locally
- Use [reverse API](https://nominatim.org/release-docs/develop/api/Reverse/) to resolve

Run:

```
docker run \
-e PBF_PATH=/data/singapore.osm.pbf \
-e REVERSE_ONLY=true \
-p 8080:8080 \
-e IMPORT_WIKIPEDIA=false \
-e NOMINATIM_PASSWORD=password \
-v nominatim-data:/var/lib/postgresql/14/main \
-v nominatim-flatnode:/nominatim/flatnode \
-v /Users/zhenya/Downloads:/data \
--name nominatim \
mediagis/nominatim:4.4
```

Open URL:

http://localhost:8080/reverse?format=jsonv2&lat=1.3119099340519775&lon=103.8887017595569

