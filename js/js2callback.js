import request from 'request';

export const getWithCallback = (cb) => {
  return request('https://en.wikipedia.org/wiki/Special:Random', (err, res, body) => {
    if (err) {
      return;
    }
    cb(body);
  });
};
