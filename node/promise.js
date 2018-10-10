const hget = require('hget');
const marked = require('marked');
const Term = require('marked-terminal');
const getRandomArticle = require('./getRandomArticle');

const printRandomArticle = () => {
  return getRandomArticle()
    .then((html) => {
      console.log('parsing raw html to markdown');
      return hget(html, {
        markdown: true,
        root: '#content',
        ignore: '.at-subscribe,.mm-comments,.de-sidebar'
      });
    })
    .then((md) => {
      console.log('converting to terminal');
      return marked(md, {
        renderer: new Term()
      });
    })
    .then(txt => console.log(txt))
    .catch(reason => console.error(reason));
};

printRandomArticle();