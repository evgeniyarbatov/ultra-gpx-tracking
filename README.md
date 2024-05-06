# GPX Route Tracking for Ultras

Track progress along a GPX route during an ultra run.

Runs in the browser and for current location displays:

- Street address of the current location
- Distance completed and remaining
- ETA to complete the route given current pace
- Download GPX file for Polar watch (limited to next 500 waypoints)

## How to use

- Add your GPX file to the server
- Create/update Dockerhub images for frontend and backend
- Deploy code to AWS with Terraform
- Load public URL in the browser on the phone

## Requirements

Install gRPC tools for NodeJS

```
npm install -g grpc-tools
```

## Run locally

```
docker compose up
```

