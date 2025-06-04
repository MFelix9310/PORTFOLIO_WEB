const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  entry: {
    main: './src/index.js',
    projectList: './src/project-list.js',
    workExperienceList: './src/work-experience-list.js',
  },
  output: {
    path: path.resolve(__dirname, '../portfolio/static/react'),
    filename: '[name]-[hash].js',
    publicPath: '/static/react/',
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
        },
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader'],
      },
    ],
  },
  optimization: {
    splitChunks: {
      chunks: 'all',
      name: 'vendors',
    },
  },
  plugins: [
    new BundleTracker({
      path: __dirname,
      filename: 'webpack-stats.json',
    }),
  ],
}; 