Run local:

```
source ~/.venv/bin/activate && (\
watchmedo auto-restart --recursive --pattern="*.py" python src/server.py \
)
```

Run container:

```
docker run -p 9090:9090 evgenyarbatov/gpx-backend:latest
```