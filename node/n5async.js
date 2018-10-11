const hget = require('hget');
const marked = require('marked');
const Term = require('marked-terminal');
const getRandomArticle = require('./getRandomArticle');

const printRandomArticle = async () => {
  try {
    const html = await getRandomArticle();
    console.log('parsing raw html to markdown');
    const md = await hget(html, {
      markdown: true,
      root: '#content',
      ignore: '.at-subscribe,.mm-comments,.de-sidebar'
    });
    console.log('converting to terminal');
    const txt = await marked(md, {
      renderer: new Term()
    });
    console.log(txt);
  } catch(reason) {
    console.error(reason);
  }
};

printRandomArticle();
