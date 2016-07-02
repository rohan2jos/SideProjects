app.controller('MainController', function($location,$scope){
    
    $scope.$location = $location;
    
    $scope.title = "Hello, Angular!"
    console.log("Welcome to codeApp");
    
    
});