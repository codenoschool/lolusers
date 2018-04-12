var express = require('express');
var path = require('path');
var app = express();

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.get('/', (req, res) => {
	res.send('Hello World!');
});

app.get('/view', (req, res) => {
	res.render('index');
})

app.listen(3000, () => {
	console.log('* Running on http://127.0.0.1:3000/ (Press CTRL + C to quit)');
});
