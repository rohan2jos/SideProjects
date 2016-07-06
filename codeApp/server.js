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
var session = require('express-session');
var mongoose = require("mongoose");



app.use(express.static(__dirname + '/public'));

// this is the connection string that specifies the mongodb location
// the name of the database in which we are going to store our data
// for this webapp
var connectionString = "mongodb://127.0.0.1:27017/codeApp";
var db = mongoose.connect(connectionString);

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
//app.use(multer());

// we will use the session here, and the session will have a password
app.use(session({
    secret: 'EnterAtYourOwnRisk',
    resave: true,
    saveUninitialized: true
}));


app.use(cookieParser());



require('./public/server/app.js')(app, db, mongoose);

var ipaddress = process.env.OPENSHIFT_NODEJS_IP || '127.0.0.1';

var port = process.env.OPENSHIFT_NODEJS_PORT || 3000;

app.listen(port, ipaddress);

