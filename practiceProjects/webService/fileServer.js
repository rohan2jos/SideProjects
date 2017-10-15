// A static file server using http
// this is a very basic server that serves static files to requests through http
 var path = require('path');
 var http = require('http');
 var fs = require('fs');
 var url = require('url');
 var mime = require('mime');

// we create a server
 var server = http.createServer();

// whenever the request comes in, we catch it and then handle the request
server.on('request', function(request, response){

});

// we need to get the server to listen on a specific port, we choose 9000
server.listen(9000);
