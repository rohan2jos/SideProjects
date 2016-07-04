angular.module("codeApp").factory("UserService", function($http, $rootScope){
    
    var service = {
        test: test,
        login: login
    }
    
    return service;
    
    function test(){
        console.log("The user service is locked and loaded");
    }
    
    function login(){
        console.log("trying to log the user in...");
    }
    
});