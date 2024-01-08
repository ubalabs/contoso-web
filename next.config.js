/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'standalone',

  // See: https://nextjs.org/docs/app/api-reference/next-config-js/images
  // Goal: Get images loaded from filesystem faster
  images: {
    loader: 'custom',
    loaderFile: './public/images/loader.js',
  },
}

module.exports = nextConfig
