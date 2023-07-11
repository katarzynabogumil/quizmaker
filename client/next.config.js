/** @type {import('next').NextConfig} */
const dotenv = require('dotenv');
dotenv.config();

const nextConfig = {
  env: {
    server_url: process.env.SERVER_URL,
    url: 'http://localhost:3000/'
  },
};

module.exports = nextConfig;
