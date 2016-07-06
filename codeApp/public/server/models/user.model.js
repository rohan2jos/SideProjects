// requiring the users file
// this will later go into the mongoose
// for now, we shall keep the users as a json file
var users = require("./user.mock.json");

module.exports = function(){
    
    // this will later go into the api endpoints
    // for now, we will just assign functions as values
    // to the keys
    var api = {
        findUserByCredentials: findUserByCredentials,
        createUser: createUser
    };
    return api;
    
    
    // when a new user signs up
    function createUser(user){
        // user is the json object that we will receive with username and password and email
        users.push(user);
    }
    
    // when a user is trying to login
    function findUserByCredentials(credentials){
        var username = credentials.username;
        var password = credentials.password;
        var userPresent = null;
        for(var u in users){
            if(users[u].username === username && users[u].password === password){
                console.log("user " + username + " has logged in successfully");
                userPresent = users[u];
                break;
            }
        }
        
        return userPresent;
    }
    
    
};