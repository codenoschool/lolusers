var express = require('express');
var request = require('request');
var path = require('path');
var app = express();

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

var hostRequest = 'http://127.0.0.1:5000/api/users';

app.get('/', (req, res) => {
	res.render('index');
});

app.get('/users', (req, res) => {
	request(hostRequest, { json: true }, (err, response, body) => {
		if (err) { console.log(err) };
		res.render('users', {
			users: body
		});
	});
});

app.listen(3000, () => {
	console.log('* Running on http://127.0.0.1:3000/ (Press CTRL + C to quit)');
});
