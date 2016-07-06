module.exports = function(app, userModel){

    // this is the api endpoints
    // the http requests are caught here
    app.post("/api/codeApp/user", createUser);
    app.post("/api/codeApp/login", loginWithCredentials);
    
    
    function createUser(req, res){
        console.log("[createUser] hit the backend, first checkpoint reached");
        var user = req.body;
        console.log("The user that is requesting to be inserted is " + user);
        var userCreated = userModel.createUser(user);
        res.json(userCreated);
    }
    
    
    
    function loginWithCredentials(req, res) {
        var credentials = req.body;
        console.log("in server");
        console.log(credentials.username);
        var currentUser = userModel.findUserByCredentials(credentials);
        res.json(currentUser);
    }
}