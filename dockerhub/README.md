First time

```
tf init
```

Postgis

```
tf apply \
-var 'image_name=gpx-postgis' \
-var 'source_path=../postgis' \
-auto-approve
```

Backend

```
tf apply \
-var 'image_name=gpx-backend' \
-var 'source_path=../backend' \
-auto-approve
```

Frontend

```
tf apply \
-var 'image_name=gpx-frontend' \
-var 'source_path=../frontend' \
-auto-approve
```