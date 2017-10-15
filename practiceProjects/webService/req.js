// requiring the libraries for a basic server
var http = require('http');
var url = require('url');

// create a http server
server = http.createServer();

server.on('request', function(req, res) {
	console.log("a new request " + req.url);
	var incomingUrl = url.parse(req.url, true);
	console.log(incomingUrl);
	

	// we will now respond to the requests
	// 200 means resource found
	// 404 is resource not found
	// so in a case where the user enters the wrong url, we respond with a 404 error message
	if(incomingUrl.path === '/hello'){		
		res.writeHead(200, {'Content-Type':'text/plain'});
		res.end('Hello World');		
	}

	if(incomingUrl.path === '/goodbye'){
		res.writeHead(200, {'Content-type':'text/plain'});
		res.end('Goodbye!');
	}else{
		// this is when the url points to a resource that is not available to the server
		// we respond with a 404 error message
		res.writeHead(404, {'Content-type':'text/plain'});
		res.end("The resource that you are looking for is not found");
	}



	// res.writeHead(200, {'Content-Type':'text/plain'});
	// res.end('Hello World');
});

// whenever somone pings our server, this is the port that they will come to
server.listen(9000);

// output on opening browser (output on console):
/*
Rohans-Air:webService rohanjoshi$ node req
a new request
*/

