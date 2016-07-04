/*
    Created by rohan2jos
    06/28/2016
*/

var express = require('express');
var app = express();
var https = require('https');
var bodyParser = require('body-parser');
var multer = require('multer');
var uuid = require('node-uuid');
var cookieParser  = require('cookie-parser');


app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(cookieParser());

app.use(express.static(__dirname + '/public'));

require('./public/server/app.js')(app, uuid);

var ipaddress = process.env.OPENSHIFT_NODEJS_IP || '127.0.0.1';

var port = process.env.OPENSHIFT_NODEJS_PORT || 3000;

app.listen(port, ipaddress);

