const path = require('path');

module.exports = {
  entry: './src/index.ts', // Entry point for your TypeScript files
  devtool: 'inline-source-map', // Enable source maps for easier debugging
  module: {
    rules: [
      {
        test: /\.ts$/, // Apply ts-loader to .ts files
        use: 'ts-loader',
        exclude: /node_modules/, // Exclude node_modules folder from transpiling
      },
    ],
  },
  resolve: {
    extensions: ['.ts', '.js'], // Allow Webpack to resolve .ts and .js files
  },
  output: {
    filename: 'bundle.js', // The output file name for the bundled JavaScript
    path: path.resolve(__dirname, 'dist'), // The output directory
  },
  devServer: {
    static: './dist', // Serve static files from the dist directory
    proxy: {
      '/api': 'http://localhost:5000', // Proxy API requests to Flask backend
    },
  },
};
