// server.js

    // set up ========================
    var express  = require('express');
    var app      = express();                               // create our app w/ express
    var mongoose = require('mongoose');                     // mongoose for mongodb
    var morgan = require('morgan');             // log requests to the console (express4)
    var bodyParser = require('body-parser');    // pull information from HTML POST (express4)
    var methodOverride = require('method-override'); // simulate DELETE and PUT (express4)

    // configuration =================

    mongoose.connect('mongodb://localhost:27017/todo', function(err, db){
        if(err){
            console.log("THE SERVER CANNOT CONNECT TO MONGO");
        }else{
            console.log("THE SESSION IS CONNECTED TO " + db);
        }
    });     // connect to mongoDB database on modulus.io

    app.use(express.static(__dirname + '/public'));                 // set the static files location /public/img will be /img for users
    app.use(morgan('dev'));                                         // log every request to the console
    app.use(bodyParser.urlencoded({'extended':'true'}));            // parse application/x-www-form-urlencoded
    app.use(bodyParser.json());                                     // parse application/json
    app.use(bodyParser.json({ type: 'application/vnd.api+json' })); // parse application/vnd.api+json as json
    app.use(methodOverride());

    // the model that gets inserted into the mongo goes here
    var Todo = mongoose.model('ToDo', {
        text: String
    });
    


    // =====  API  =====

    // Whenever we get a request, we handle that here
    // we are defining our api and handling it here
    // The api endpoints are as required for add, lookup, delete

    // this is to retrieve all the todos that have been previously stored
    app.get('/api/todos', function(req, res){
        Todo.find(function(err, todos){
            if(err){
                console.log("Encountered an error in the lookup, " + err);
                res.send(err);
            }
            res.json(todos);
            // the above line tells us that the todos have been found, and we return them in JSON format
        });
    });

    // this is to add a new todo into the model and the mongo
    // The api endpoint uses post to insert into the schema/model/mongo
    // the req parameter will hold the todo that we want to add through AJAX
    // We will have to extract it using req.bosy
    app.post('/api/todos', function(req, res){
    
        // create a todo, so we package it into json with the incoming text
        // and the format is as we declared above
        Todo.create({
            text: req.body.text,
            done: false
        }, function(err, todo){
            // if this, then there was an error in creating
            if(err){
                console.log("Error in creating todo, " + err);
                res.send(err);
            }
            
            // if code comes here, then the todo is inserted
            // We now need to fetch all the previous todos with the new todo
            // that was just inserted
            Todo.find(function(err, todos){
                if(err){
                    console.log("error in retrieving after todo created " + err);
                    res.send(err);
                }
                // if here, the todos will be retrieved, so we return them in json
                // format
                res.json(todos);
            });
        })
    });

    // this is to remove a todo if the user does not want to keep it
    // the endpoint is delete
    app.delete('/api/todos/:todo_id', function(req, res){
        
        Todo.remove({_id: req.params.todo_id}, function(err, model){
            if(err){
                console.log("PROBLEM WHILE DELETING MODEL");
                res.send(err);
            }
            Todo.find(function(err, todos){
                if(err){
                    console.log("=====error in retrieving after deleting=====");
                }
                res.json(todos);
            });
        });
        
        
        // we know what todo we want to remove and it comes as an AJAX request
        // We just have to get the id and send it as a JSON object and mongo will
        // handle the deletion based on the id
        /*Todo.delete({
            _id: req.params.todo_id
        }, function(err, todo){
            if(err){
                console.log("There was an error when deleting the todo, " + err);
                res.send(err);
            }
            
            Todo.find(function(err, todos){
                if(err){
                    console.log("There was an error while retrieving the todos after deletion, " + err);
                    res.send(err);
                }
                console.log("Todos fetched successfully after deletion");
                res.json(todos);
            });
        });*/
    });

    // adding the page that the server needs to serve
    // here, we specify what html page needs to be rendered when a particular url is hit
    app.get('*', function(req, res){
        res.sendFile('./public/index.html');
    });



    // listen (start app with node server.js) ======================================
    app.listen(8080);
    console.log("App listening on port 8080");