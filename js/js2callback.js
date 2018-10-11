const RANDOM_URL = 'https://commons.wikimedia.org/wiki/Special:Random/File';

export const getRandom = async (url) => {
  console.log('executing request inside async function');
  return await fetch(url, {
  	mode: 'no-cors'
  });
};

export const getMany = async () => {
  const urls = Array(100).fill(RANDOM_URL);
  return await Promise.all(urls.map((url) => {
    return getRandom(url);
  }));
}

