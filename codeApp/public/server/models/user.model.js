// requiring the users file
// this will later go into the mongoose
// for now, we shall keep the users as a json file
var q = require('q');
var uuid = require('node-uuid');


//var users = require("./user.mock.json");



module.exports = function(db, mongoose){

    
    var UserSchema = require("./user.schema.server.js")(mongoose);
    var UserModel = mongoose.model('Users', UserSchema);
    // this will later go into the api endpoints
    // for now, we will just assign functions as values
    // to the keys
    var api = {
        findUserByCredentials: findUserByCredentials,
        createUser: createUser,
        findUserByUsername: findUserByUsername
    };
    return api;
    
    
    function findUserByUsername(username){
        var deferred = q.defer();
        
        console.log("[findUserByUsername - model] inside find user by username");
        UserModel.findOne({username: username}, function(err, doc){
            if(err){
                console.log("[findUserByUsername - model] Error in retrieving");
                deferred.reject(err);
            }
            else{
                if(doc == null){
                    console.log("[findUserByUsername - model] Going back to the service to create new user, user found is " + doc);   
                }else{
                    console.log("[findUserByUsername - model] Going back to the service, user found is " + doc);
                }
                deferred.resolve(doc);
            }
        });
        return deferred.promise;
    }
    
    
    // when a new user signs up
    function createUser(user){
        // user is the json object that we will receive with username and password and email
        //users.push(user);
        console.log("[createUser - model] trying to create a new user");
        var username = user.username;
        var password = user.username;
        var email = user.email;
        
        var userToInsert = {
            username: username,
            password: password,
            email: email
        }
        
        var deferred = q.defer();
        
        UserModel.create(userToInsert, function(err, doc){
            if(err){
                console.log("[createUser - model] There was an issue during creation of the user");
            }else{
                deferred.resolve(doc);
            }
        });
        return deferred.promise();
    }
    
    // when a user is trying to login
    function findUserByCredentials(credentials){
        var username = credentials.username;
        var password = credentials.password;
        var userPresent = null;
//        for(var u in users){
//            if(users[u].username === username && users[u].password === password){
//                console.log("user " + username + " has logged in successfully");
//                userPresent = users[u];
//                break;
//            }
//        }
//        
        return userPresent;
    }
    
    
    
    
};