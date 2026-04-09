const http = require('http');
const fs = require('fs');
const path = require('path');
const https = require('https');

// ── CONFIG ──
const PORT = 3000;
// Set your API key here or as an environment variable:
// Windows: set ANTHROPIC_API_KEY=your_key_here
// Mac/Linux: export ANTHROPIC_API_KEY=your_key_here
const API_KEY = process.env.ANTHROPIC_API_KEY || 'YOUR_API_KEY_HERE';

// ── MIME TYPES ──
const MIME = {
  '.html': 'text/html',
  '.css':  'text/css',
  '.js':   'application/javascript',
  '.json': 'application/json',
  '.png':  'image/png',
  '.ico':  'image/x-icon',
};

// ── ANTHROPIC CALL ──
function callAnthropic(body) {
  return new Promise((resolve, reject) => {
    const data = JSON.stringify(body);
    const req = https.request({
      hostname: 'api.anthropic.com',
      path: '/v1/messages',
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': API_KEY,
        'anthropic-version': '2023-06-01',
        'Content-Length': Buffer.byteLength(data),
      },
    }, res => {
      let raw = '';
      res.on('data', chunk => raw += chunk);
      res.on('end', () => {
        try { resolve({ status: res.statusCode, body: JSON.parse(raw) }); }
        catch (e) { reject(e); }
      });
    });
    req.on('error', reject);
    req.write(data);
    req.end();
  });
}

// ── SERVER ──
const server = http.createServer(async (req, res) => {
  // CORS
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') { res.writeHead(204); res.end(); return; }

  // API PROXY
  if (req.method === 'POST' && req.url === '/api/recommend') {
    let body = '';
    req.on('data', chunk => body += chunk);
    req.on('end', async () => {
      try {
        const parsed = JSON.parse(body);
        parsed.max_tokens = 2000;
        const result = await callAnthropic(parsed);
        res.writeHead(result.status, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify(result.body));
      } catch (err) {
        res.writeHead(500, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: err.message }));
      }
    });
    return;
  }

  // STATIC FILES
  let filePath = req.url === '/' ? '/index.html' : req.url;
  filePath = path.join(__dirname, filePath);

  fs.readFile(filePath, (err, data) => {
    if (err) {
      res.writeHead(404);
      res.end('Not found');
      return;
    }
    const ext = path.extname(filePath);
    res.writeHead(200, { 'Content-Type': MIME[ext] || 'text/plain' });
    res.end(data);
  });
});

server.listen(PORT, () => {
  console.log(`\n✦ FOR THE CULTURE ✦`);
  console.log(`Server running at http://localhost:${PORT}`);
  if (API_KEY === 'YOUR_API_KEY_HERE') {
    console.log(`\n⚠️  No API key set! Set it with:`);
    console.log(`   Windows: set ANTHROPIC_API_KEY=your_key`);
    console.log(`   Mac/Linux: export ANTHROPIC_API_KEY=your_key`);
    console.log(`   Then restart: node server.js\n`);
  } else {
    console.log(`✓ API key loaded\n`);
  }
});