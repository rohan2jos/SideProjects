angular.module("codeApp").factory("UserService", function($http, $rootScope){
    
    var service = {
        setCurrentUser: setCurrentUser,
        getCurrentUser: getCurrentUser,
        createUser: createUser,
        login: login
    }
    
    return service;
    
    
    // we will centralize the process of setting currentUser
    // The service will receive the user to be set as the current
    // user from the respective controller
    function setCurrentUser(user){
        $rootScope.currentUser = user;
    }
    
    function getCurrentUser(){
        return $rootScope.currentUser;
    }
    
    // we will now send the requests to the backend
    // these requests will be GET,POST,DELETE,PUT
    // after every function, we will return the data so that
    // it can be manipulated in the respective controller
    function createUser(user){
        console.log("The front end is trying to request server to create user " + user.username);
        return $http.post("/api/codeApp/user", user);
    }
    
    // this will request 'findUserByCredentials' in the server to validate the login
    function login(username, password){
        
        var credentials = {
            username: username,
            password: password
        }
        
        console.log("front end is trying to login the user " + username);
        return $http.post("/api/codeApp/login", credentials);
    }
    
});