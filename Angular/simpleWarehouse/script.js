// angular controller

/*
  Initial setup:
  1 Declare the angular app and set a name
  2 In the html element of the index page, declare the directive ng-app (This tells us that this is an angular js application)
*/

var app = angular.module("computer", ['ngRoute'])
// we will now describe the config using the routes
// the dependancy has been included above

// the $routeProvider below is the dependancy injection and the dependancy has
// been passed to the function
// notice that it starts with .
// This means that we are chaining it to the app declared above

.config('$routeProvider', function($routeProvider){
  $routeProvider
  .when("/main", {
    templateUrl: 'main.html',
    controller: 'MainCtrl'
  });
})

// chaining controller to the app declared above
// defining the controller

.controller('MainCtrl', [function(){
  console.log("This is the main controller");
}]);