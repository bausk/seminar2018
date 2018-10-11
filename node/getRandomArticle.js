const request = require('request');

module.exports = () => {
  return new Promise((resolve, reject) => {
    console.log('executing request inside promise');
    return request('https://en.wikipedia.org/wiki/Special:Random', (err, res, body) => {
      console.log('returning');
      if (err) {
        reject(err);
        return;
      }
      console.log('resolving');
      resolve(body);
    });
  });
};
