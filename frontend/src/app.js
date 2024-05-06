const express = require('express');
const winston = require('winston');

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

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/public/index.html');
});

app.get('/location', async (req, res) => {
  const { lat, lng } = req.query;
  logger.info(`Location: lat=${lat}, lng=${lng}`);

  const request = {
    lat: lat,
    lng: lng,
  };

  const requests = [
    new Promise((resolve, reject) => {
      gRPCClient.getAddress(request, (err, response) => {
        if (err) {
          reject(err);
        } else {
          resolve(response);
        }
      });
    }),
    new Promise((resolve, reject) => {
      gRPCClient.getRemainginDistance(request, (err, response) => {
        if (err) {
          reject(err);
        } else {
          resolve(response);
        }
      });
    }),
  ];

  Promise.all(requests)
    .then(responses => {
      res.json({ lat: lat, lng: lng, responses: responses });
    })
    .catch(error => {
      res.json({ error: error });
    });
});

app.listen(port, () => {
  logger.info(`App listening at http://localhost:${port}`);
});
