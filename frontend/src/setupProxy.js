const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function(app) {
  // Proxy requests with '/api' prefix to the Flask backend
  app.use(
    '/api',
    createProxyMiddleware({
      target: 'http://backend:5000', // Change this to your Flask backend's address
      changeOrigin: true,
    })
  );
};