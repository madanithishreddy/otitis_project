/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    appDir: true,
    metadataBase: process.env.NEXT_PUBLIC_API_URL || "http://localhost:3000",
  },
  images: {
    dangerouslyAllowSVG: true,
    domains: [
      "localhost",
      "ui-avatars.com" // Added ui-avatars.com to the allowed domains
    ],
  },
};

module.exports = nextConfig;
