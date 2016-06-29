/*
    Created by rohan2jos
    06/28/2016
*/

var app = angular.module('codeApp', ['ngRoute']);

app.config(['$routeProvider', function($routeProvider){
    $routeProvider
        .when('/home', {
            templateUrl: "./views/home.html",
            controller: "homeController"
        })
        .when('/about', {
            templateUrl: "./views/about.html",
            controller: "aboutController"
        })
        .otherwise({
            redirectTo: "/home"
        });
}]);