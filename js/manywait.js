async function k(v) {
	return v * 3;
}

async function asyncFun () {
  var value = await Promise.resolve(1);
  let res = await k(value)
    .then(x => x + 5)
    .then(x => x / 2);
  return res;
}

asyncFun().then(x => console.log(`x: ${x}`));
