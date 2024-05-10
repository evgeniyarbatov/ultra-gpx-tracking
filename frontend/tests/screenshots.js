const puppeteer = require('puppeteer');

const locations = [
  { latitude: 1.3100792, longitude: 103.8965681, name: 'Home'},
  { latitude: 1.422383, longitude: 103.864101, name: 'Yishun Dam'},
  { latitude: 1.4125291681929364, longitude: 103.786552508942731, name: 'Mandai Rd'},
  { latitude: 1.3508579544650554, longitude: 103.67896257875732, name: 'NIE'},
  { latitude: 1.2984888134729362, longitude: 103.76023767100665, name: 'West Coast Park'},
];

describe('Location test', () => {
  let browser;
  let page;

  beforeAll(async () => {
    browser = await puppeteer.launch();
    page = await browser.newPage();
  });

  afterAll(async () => {
    await browser.close();
  });

  it('set location and take screenshot', async () => {
    await page.goto('https://arbatov.me/sg200/index.html');

    for (const location of locations) {
      // Set the geolocation
      await page.setGeolocation({ latitude: location.latitude, longitude: location.longitude });

      // Wait for the button to be visible
      await page.waitForSelector('#getLocationInfo');

      // Click the button
      await page.click('#getLocationInfo');

      // Wait for page to load
      await page.waitForFunction(() => {
        const div = document.querySelector('#container');
        return div && div.textContent.trim() !== '';
      });

      // Take a screenshot with location name
      await page.screenshot({ path: `tests/screenshots/${location.name.replace(/\s+/g, '_')}.png` });
    }
  });
});
