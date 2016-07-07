module.exports = function(app, userModel){

    // this is the api endpoints
    // the http requests are caught here
    app.post("/api/codeApp/user", createUser);
    app.post("/api/codeApp/login", loginWithCredentials);
    
    
    function createUser(req, res){
//        console.log("[createUser] hit the backend, first checkpoint reached");
//        var user = req.body;
//        console.log("The user that is requesting to be inserted is " + user);
//        var userCreated = userModel.createUser(user);
//        
        var newUser = req.body;
        
        userModel.findUserByUsername(newUser.username)
            .then(function(user){
            if(user == null){
                return userModel.createUser(newUser);
            }else{
                res.json(null);
            }
        }, function(err){
            res.status(400).send(err);
        }).then(function(user){
            if(user){
                req.login(user, function(err){
                    if(err){
                        res.status(400).send(err);
                    }else{
                        res.json(user);
                    }
                });
            }
        }, function(err){
            res.status(400).send(err);
        });
        
    }
    
    
    
    function loginWithCredentials(req, res) {
        var credentials = req.body;
        console.log("in server");
        console.log(credentials.username);
        var currentUser = userModel.findUserByCredentials(credentials);
        res.json(currentUser);
    }
}