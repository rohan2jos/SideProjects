/*
    Created by rohan2jos
    06/28/2016
*/

var app = angular.module('codeApp', ['ngRoute', 'ngAnimate', 'ngToast']);

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
        .when('/work', {
            templateUrl: "./views/work.html",
            controller: "workController"
        })
	.when('/contact', {
	templateUrl: './views/contact.html',
	controller: "contactController"	
	})
    .when('/register', {
        templateUrl: "./views/register.html",
        controller: "registerController"
    })
	.when('/login', {
	templateUrl: './views/login.html',
	controller: "loginController"
	})
        .otherwise({
            redirectTo: "/home"
        });
}]);
