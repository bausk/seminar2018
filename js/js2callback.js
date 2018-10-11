export const RANDOM_URL = 'https://dog.ceo/api/breeds/image/random';

export const getRandom = async (url) => {
  console.log('executing request inside async function');
  return await fetch(url, {
  });
};

export const getMany = async () => {
  const urls = Array(10).fill(RANDOM_URL);
  return await Promise.all(urls.map((url) => {
    return getRandom(url);
  }));
};


export const display = async (results) => {
  await results.map(async (result) => {
    const json = await result.json();
    const x = document.createElement("IMG");
    x.setAttribute("src", json.message);
    x.setAttribute("width", 200);
    document.body.appendChild(x);
  });
};

export const help = () => {
  console.log("const result = await foo.getMany(); await foo.display(result);");
};

export const onclick = async () => {
  const result = await getMany();
  await display(result);
};
