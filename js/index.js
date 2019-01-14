import * as rx from 'rxjs';

export * as rx from 'rxjs'
export * from './js1fib';
export * from './js2callback';

const url = 'https://dog.ceo/api/breeds/image/random';

const { scan } = rx.operators;

const handle = (value) => {
	console.log(value)
};

export let a;

export const start = (e) => {
	a = rx.of(url);
	a.subscribe(handle);
	debugger;
};
