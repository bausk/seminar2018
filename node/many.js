const request = require('request');

const execute = (url, cb) => {
	return request(url, cb);
}

const callback = (err, res, body) => {
	console.log(`${res.request.href}`);
}

const RANDOM_URL = 'https://commons.wikimedia.org/wiki/Special:Random/File';

const URLS = Array(10).fill(RANDOM_URL);
URLS.map((url) => {
	execute(url, callback);
});
