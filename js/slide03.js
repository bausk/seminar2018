
async function asyncFun () {
  var value = await Promise
    .resolve(1)
    .then(x => x * 3)
    .then(x => x + 5)
    .then(x => x / 2);
  return value;
}

function main() {
	asyncFun().then(x => console.log(`x: ${x}`));
}

