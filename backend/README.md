Run local:

```
source ~/.venv/bin/activate && (\
python src/server.py \
)
```

Run container:

```
docker run -p 9090:9090 evgenyarbatov/gpx-backend:latest
```