const express = require('express');
const winston = require('winston');

const port = 8080;

const app = express();

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

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/public/index.html');
});

app.get('/location', (req, res) => {
  const { lat, lon } = req.query;
  logger.info(`Location: lat=${lat}, lng=${lon}`);
  res.json({ lat: lat, lng: lon });
});

app.listen(port, () => {
  logger.info(`App listening at http://localhost:${port}`);
});
