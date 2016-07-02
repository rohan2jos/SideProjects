angular.module("codeApp").controller("headerController", function($location,$rootScope,$scope){
    
    $scope.logout = logout;
    $scope.test = test;
    
    console.log("Header controller loaded!");
    
    console.log("header controller says " + $rootScope.user);
    
    function test(){
        console.log("reaching");
    }
    
    function logout(){
        console.log("logging out");
        $rootScope.currentUser = null;
    }
    
});
