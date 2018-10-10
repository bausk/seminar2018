const request = require('request');

const execute = (url, cb) => {
	return request(url, cb);
}

const callback = (err, res, body) => {
	console.log(`${res.request.href}`);
}

const RANDOM_URL = 'https://commons.wikimedia.org/wiki/Special:Random/File';

const req = execute(RANDOM_URL, callback);

