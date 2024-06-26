const express = require('express');
const winston = require('winston');
const cors = require('cors');

const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');

const port = process.env.SERVER_PORT || 8080;
const gRPCServerURL = process.env.GRPC_SERVER || 'localhost:9090'

const packageDefinition = protoLoader.loadSync(
  './src/gpxtracker/gpxtracker.proto',
  {
    keepCase: true,
    longs: String,
    enums: String,
    defaults: true,
    oneofs: true
  }
);

const gpxtracker_proto = grpc.loadPackageDefinition(packageDefinition).main;

const gRPCClient = new gpxtracker_proto.GPXTracker(
  gRPCServerURL,
  grpc.credentials.createInsecure(),
);

const customFormat = winston.format.printf(({ level, message, timestamp }) => {
  return JSON.stringify({ timestamp, message  });
});

const logger = winston.createLogger({
  format: winston.format.combine(
    winston.format.timestamp(),
    customFormat
  ),
  transports: [
    new winston.transports.Console()
  ]
});

const app = express();

app.use(cors())

app.get(/^\/(index.html)?$/, (req, res) => {
  res.sendFile(__dirname + '/public/index.html');
});

app.get('/location', async (req, res) => {
  logger.info(`Get location`);

  const { lat, lng } = req.query;

  const request = {
    lat: lat,
    lng: lng,
  };

  new Promise((resolve, reject) => {
    gRPCClient.GetLocationInfo(request, (err, response) => {
      if (err) {
        reject(err);
      } else {
        resolve(response);
      }
    });
  }).then(response => {
    const result = Object.assign(
      {}, 
      { 
        lat: lat, 
        lng: lng,
      },
      response,
    );
    res.json(result);
  })
  .catch(error => {
    res.json({ error: error });
  });
});

app.get('/gpx', (req, res) => {
  logger.info(`Get GPX`);

  const { lat, lng } = req.query;

  const request = {
    lat: lat,
    lng: lng,
  };

  new Promise((resolve, reject) => {
    gRPCClient.GetGPXFile(request, (err, response) => {
      if (err) {
        reject(err);
      } else {
        resolve(response);
      }
    });
  }).then(response => {
    res.set('Content-Type', 'application/xml');
    res.send(response.xml);
  })
  .catch(error => {
    res.json({ error: error });
  });
});

app.listen(port, () => {
  logger.info(`App listening at http://localhost:${port}`);
});
